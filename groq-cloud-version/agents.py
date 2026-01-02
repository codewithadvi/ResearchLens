import os
import warnings
from typing import Type
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from linkup import LinkupClient
from crewai import Agent, Task, Crew, Process, LLM
from crewai.tools import BaseTool

# Suppress CrewAI signal handler warnings in Streamlit
warnings.filterwarnings("ignore", message=".*signal only works in main thread.*")

# Load environment variables
load_dotenv()

# Disable CrewAI telemetry to avoid signal handler warnings with Streamlit
os.environ["OTEL_SDK_DISABLED"] = "true"

# --- 1. SETUP LLM (GROQ ONLY - Cloud Optimized) ---
def get_llm_client(use_fast_model=False):
    """Uses Groq Cloud API (free tier with generous limits)"""
    groq_key = os.getenv("GROQ_API_KEY")
    if not groq_key:
        raise ValueError(
            "GROQ_API_KEY not found. Get free key from https://console.groq.com\n"
            "Add to .env: GROQ_API_KEY=your_key"
        )
    
    # Use faster, smaller model for final task to avoid rate limits
    model = "groq/llama-3.1-8b-instant" if use_fast_model else "groq/llama-3.3-70b-versatile"
    
    return LLM(
        model=model,
        api_key=groq_key
    )

# --- 2. DEFINE TOOLS ---
class LinkUpSearchInput(BaseModel):
    query: str = Field(description="The search query to perform")
    depth: str = Field(default="deep", description="Use 'deep' for research papers")

class LinkUpSearchTool(BaseTool):
    name: str = "LinkUp Search"
    description: str = "Search for specific technical details, future work sections, and research gaps."
    args_schema: Type[BaseModel] = LinkUpSearchInput

    def _run(self, query: str, depth: str = "deep") -> str:
        try:
            linkup_client = LinkupClient(api_key=os.getenv("LINKUP_API_KEY"))
            return str(linkup_client.search(query=query, depth=depth, output_type="searchResults"))
        except Exception as e:
            return f"Error: {str(e)}"

# --- 3. DEFINE CREW ---
def create_research_crew(query: str):
    """
    Universal Research Crew that produces detailed, technical reports for ANY topic.
    Optimized for Groq Cloud API (fast inference, free tier).
    """
    linkup_search_tool = LinkUpSearchTool()
    client = get_llm_client()

    # --- AGENT 1: The Miner (Universal) ---
    web_searcher = Agent(
        role="Technical Entity Miner",
        goal="Extract specific PROPER NOUNS (Models, Algorithms, Datasets) and 'Future Work' quotes related to the topic.",
        backstory="You are a deep-dive researcher. You do not care about general summaries. You hunt for capitalized names (e.g., 'ResNet', 'CRISPR', 'Black-Scholes'). You extract specific metrics and quotes from the Conclusion sections of papers.",
        verbose=True,
        tools=[linkup_search_tool],
        llm=client,
    )

    # --- AGENT 2: The Analyst (Universal) ---
    research_analyst = Agent(
        role="Research Gap Analyst",
        goal="Analyze the findings to identify the 'Novelty Gap'. What combination has NOT been tried?",
        backstory="You are a PhD Advisor. You look at the entities found. If you see Method A and Method B exist but haven't been combined, you identify that as the Research Gap. You look for contradictions between papers.",
        verbose=True,
        llm=client,
    )

    # --- AGENT 3: The Writer (Universal) ---
    technical_writer = Agent(
        role="Principal Investigator",
        goal="Write a detailed Technical Survey with clear sections.",
        backstory="You write comprehensive reports. You MUST include sections for 'State-of-the-Art', 'Limitations', and 'Future Work'. You use the specific names found by the Miner.",
        verbose=True,
        llm=client,
    )

    # --- AGENT 4: The Publisher (Universal Fix) ---
    # Use faster model to avoid rate limits on final formatting task
    fast_client = get_llm_client(use_fast_model=True)
    peer_reviewer = Agent(
        role="Final Publisher",
        goal="Output the FINAL, EXTENDED Report. Do not summarize.",
        backstory="You are a Publisher. Your job is to take the draft and the raw data and PRINT THE FULL FINAL DOCUMENT. You do not give feedback. You output the final 1000+ word article.",
        verbose=True,
        llm=fast_client,
    )

    # --- TASKS (Dynamic based on {query}) ---
    
    # Task 1: Search
    search_task = Task(
        description=f"""
        Search for: "{query}".
        
        **MANDATORY EXTRACTION TARGETS:**
        1. **Specific Methodologies**: Find the specific names of the leading techniques used in this field.
        2. **Benchmarks & Metrics**: What datasets or standards are used to measure success?
        3. **Future Work Scraper**: Find quotes where authors admit limitations (e.g., "Our method fails at X").
        4. **Contradictions**: Find papers that disagree with each other.
        """,
        agent=web_searcher,
        expected_output="A detailed list of specific Models, Methods, and Quotes found.",
        tools=[linkup_search_tool]
    )

    # Task 2: Analysis
    analysis_task = Task(
        description=f"""
        Analyze the search results for: "{query}".
        
        1. **Matrix Comparison**: Compare the identified methods (e.g., Efficiency vs Accuracy).
        2. **Identify the Gap**: Based on the "Future Work" quotes, what is the biggest unsolved problem?
        3. **Proposed Innovation**: Suggest a novel combination of the identified methods.
        """,
        agent=research_analyst,
        expected_output="Technical analysis defining the State of the Art and the Research Gap.",
        context=[search_task]
    )

    # Task 3: Draft
    writing_task = Task(
        description="""
        Write the Technical Literature Survey.
        
        **REQUIRED SECTIONS:**
        1. **State-of-the-Art (SOTA)**: Discuss the specific methods found.
        2. **Discordance & Conflicts**: What do different papers disagree on?
        3. **Future Work & Research Gaps**: A dedicated section proposing specific new research directions.
        
        Use specific citations and bold key terms.
        """,
        agent=technical_writer,
        expected_output="A full draft of the report.",
        context=[analysis_task]
    )

    # Task 4: Publish (The Fix)
    review_task = Task(
        description="""
        **FINAL OUTPUT INSTRUCTION:**
        
        Your job is to generate the **Final Complete Report**.
        
        1. Take the draft from the Writer.
        2. If it is too short, EXPAND it using the raw search data.
        3. Ensure specific names (Models/Algorithms) are used, not generic terms.
        4. **OUTPUT THE FULL DOCUMENT.** Do not just say "Here is the report". Write the actual report starting with the Title.
        """,
        agent=peer_reviewer,
        expected_output="The complete, fully written Technical Survey in Markdown format.",
        context=[writing_task, search_task] 
    )

    # --- CREATE CREW ---
    crew = Crew(
        agents=[web_searcher, research_analyst, technical_writer, peer_reviewer],
        tasks=[search_task, analysis_task, writing_task, review_task],
        process=Process.sequential,
        verbose=True
    )

    return crew

# --- 4. RUN RESEARCH ---
def run_research(query: str) -> str:
    """Execute the research workflow and return the final report."""
    crew = create_research_crew(query)
    result = crew.kickoff(inputs={"query": query})
    return str(result)
