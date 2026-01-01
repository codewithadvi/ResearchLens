# Deep Research MCP - AI-Powered Research Gap Analyzer

An intelligent research tool that conducts automated literature reviews and identifies research gaps using multi-agent AI. **Fully free, open-source, and deployable** with your choice of two approaches.

##  Features

-  **4-Agent AI Research System** - Specialized agents for searching, analyzing, and synthesizing research
-  **Research Gap Detection** - Identifies unexplored combinations and contradictions in research
-  **Academic Paper Search** - Integrates with LinkUp API for deep paper discovery
-  **Multi-Format Export** - JSON, Markdown, PDF exports of research findings
-  **Local Development** - Run with Ollama + DeepSeek-R1 7B for best quality (GPU optional)
-  **Cloud Deployment** - Deploy free to Streamlit Cloud with Groq API
-  **Dual Mode** - Switch between local Ollama and Groq API with one config change
- 🛠️**MCP Support** - Model Context Protocol server for IDE integration (optional)
-  **Fully Free** - No credit card needed, uses free tiers of all APIs

---

## 🏗️ Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                    STREAMLIT WEB INTERFACE                      │
│                  (app.py - User Chat & Export)                  │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│                    CREWAI ORCHESTRATION                          │
│                  (agents.py - 4 Agent System)                   │
│                                                                  │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │ Agent 1: Literature Reviewer                             │  │
│  │   → Searches for papers using LinkUp API                │  │
│  │   → Extracts models, algorithms, datasets               │  │
│  └──────────────────┬───────────────────────────────────────┘  │
│                     │ (task context)                            │
│  ┌──────────────────▼───────────────────────────────────────┐  │
│  │ Agent 2: Methodology Analyst                             │  │
│  │   → Analyzes extracted methodologies                     │  │
│  │   → Creates comparison matrix                            │  │
│  └──────────────────┬───────────────────────────────────────┘  │
│                     │ (task context)                            │
│  ┌──────────────────▼───────────────────────────────────────┐  │
│  │ Agent 3: Research Gap Analyst                            │  │
│  │   → Identifies missing combinations                      │  │
│  │   → Detects contradictions & conflicts                  │  │
│  └──────────────────┬───────────────────────────────────────┘  │
│                     │ (task context)                            │
│  ┌──────────────────▼───────────────────────────────────────┐  │
│  │ Agent 4: Report Writer                                   │  │
│  │   → Synthesizes final comprehensive report               │  │
│  │   → Formats with SOTA, Gaps, Future Work sections       │  │
│  └──────────────────────────────────────────────────────────┘  │
└────────────────────────┬─────────────────────────────────────────┘
                         │
        ┌────────────────┼────────────────┐
        ▼                ▼                ▼
    ┌────────┐    ┌──────────┐    ┌──────────┐
    │ Ollama │    │  Groq    │    │ LinkUp   │
    │(Local) │    │ (Cloud)  │    │   API    │
    └────────┘    └──────────┘    └──────────┘
```

### Data Flow

```
User Query
    │
    ▼
[Streamlit UI] ──────► [CrewAI Crew]
    ▲                       │
    │                   ┌───┼───┐
    │                   ▼   ▼   ▼
    │            Agent Agents  Agents
    │                   │   │   │
    │          ┌────────┼───┼───┘
    │          ▼        ▼   ▼
    │      ┌─────┐  ┌──────┐
    │      │LinkUp│  │LLM   │
    │      │(Web) │  │API   │
    │      └─────┘  └──────┘
    │          │        │
    └──────────┴────────┘
      (Search Results + Analysis)
            │
            ▼
      [Final Report]
            │
            ▼
    [Export: JSON/MD/PDF]
```

---

## 🚀 User Flow

```
START
  │
  ▼
┌─────────────────────────────────┐
│ Visit Streamlit Web App         │
│ (Local: localhost:8501)         │
│ (Cloud: yourapp.streamlit.app)  │
└────────────┬────────────────────┘
             │
             ▼
┌─────────────────────────────────┐
│ Enter Research Topic            │
│ Example:                        │
│ "quantum error correction in    │
│  superconducting qubits"        │
└────────────┬────────────────────┘
             │
             ▼
┌─────────────────────────────────┐
│ System Workflow:                │
│ 1. Search papers (LinkUp)       │
│ 2. Extract methodologies (LLM)  │
│ 3. Identify gaps (LLM)          │
│ 4. Generate report (LLM)        │
│ ⏱️ Takes 1-2 minutes           │
└────────────┬────────────────────┘
             │
             ▼
┌─────────────────────────────────┐
│ View Research Report            │
│ • State-of-the-Art (SOTA)       │
│ • Research Gaps Identified      │
│ • Future Work Suggestions       │
│ • Methodology Comparison        │
└────────────┬────────────────────┘
             │
             ▼
┌─────────────────────────────────┐
│ Export Results                  │
│ ├─ JSON (structured data)       │
│ ├─ Markdown (readable)          │
│ └─ PDF (formatted document)     │
└────────────┬────────────────────┘
             │
             ▼
┌─────────────────────────────────┐
│ View Research History (Sidebar) │
│ • Previous queries              │
│ • Reload past results           │
│ • Clear history                 │
└────────────┬────────────────────┘
             │
             ▼
           END
```

---

## 📦 Two Deployment Approaches

### Approach 1: Local Development (Best Quality)

**Use this for development on your computer**

```
Your Machine
    │
    ├─ Streamlit (web UI on port 8501)
    ├─ CrewAI (agent orchestration)
    ├─ Ollama (local LLM - best quality)
    └─ LinkUp API (paper search)
```

**Requirements:**
- Python 3.10+
- Ollama installed locally
- 8GB RAM minimum (16GB recommended for smooth operation)
- Optional: GPU for faster inference

**Steps:** See [Local Setup](#local-setup-with-ollama) section below

---

### Approach 2: Cloud Deployment (Free & Easy)

**Use this to deploy publicly on Streamlit Cloud**

```
GitHub (Your Code)
    │
    ▼
Streamlit Cloud
    │
    ├─ Streamlit (web UI - hosted)
    ├─ CrewAI (agent orchestration)
    ├─ Groq Cloud API (fast LLM - free tier)
    └─ LinkUp API (paper search)
```

**Benefits:**
- ✅ Fully free (Groq + LinkUp free tiers)
- ✅ No server costs
- ✅ Publicly accessible
- ✅ Auto-deploy on GitHub push
- ✅ Fast inference (Groq's optimization)

**Steps:** See [Cloud Deployment](#cloud-deployment-to-streamlit-cloud) section below

---

## 🗂️ Project Structure

### Root Directory (Essential Files Only)

```
deep-research-mcp/
├── README.md               ← Complete guide (you are here!)
├── server.py               ← MCP server for IDE integration (optional)
└── Two approaches below ⬇️
```

### Approach 1: Local Development (Ollama)

```
local-ollama-version/
├── app.py                  ← Streamlit web interface
├── agents.py               ← CrewAI with Ollama + Groq fallback
├── requirements.txt        ← Dependencies (streamlit, crewai, etc.)
├── .env.example            ← Template for API keys
├── .gitignore              ← Protects .env from git
└── SETUP_LOCAL.md          ← 10-minute setup guide
```

### Approach 2: Cloud Deployment (Groq)

```
groq-cloud-version/
├── app.py                  ← Streamlit web interface
├── agents.py               ← CrewAI with Groq-only setup
├── requirements.txt        ← Dependencies (same as local)
├── .env.example            ← Template for API keys
├── .gitignore              ← Protects .env from git
└── SETUP_CLOUD.md          ← 5-minute deployment guide
```

**Key Differences:**
- `local-ollama-version/agents.py`: Ollama first → Groq fallback (best quality)
- `groq-cloud-version/agents.py`: Groq only (cloud optimized, faster startup)

---

## 🔧 Setup Instructions

### Prerequisites

```bash
# Check Python version (3.10+ required)
python --version

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
.\venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Local Setup with Ollama

**Best for development - highest quality reasoning**

#### Step 1: Install Ollama

1. Download from https://ollama.ai
2. Install and run: `ollama serve` (keeps it running in background)

#### Step 2: Pull DeepSeek-R1 Model

```bash
ollama pull deepseek-r1:7b
```

This downloads ~4.7GB (first run only). Subsequent runs use cached model.

#### Step 3: Get API Keys

**LinkUp API** (required):
- Visit https://linkup.so
- Sign up for free
- Copy your API key

#### Step 4: Configure Environment

Create `.env` file in project root:

```
LINKUP_API_KEY=your_linkup_api_key_here
GROQ_API_KEY=your_groq_api_key_here
```

(GROQ_API_KEY is fallback for cloud deployment - optional locally)

#### Step 5: Run Locally

```bash
streamlit run app.py
```

Opens at `http://localhost:8501`

**Performance Notes:**
- GPU available: ~30 seconds per query
- CPU only: ~2-5 minutes per query
- First run may be slower (model initialization)

---

### Cloud Deployment to Streamlit Cloud

**Deploy for free to public internet**

#### Option A: From Main Folder (Recommended for Portfolio)

If you want automatic Ollama→Groq fallback:

1. **Push to GitHub:**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/YOUR_USERNAME/deep-research-mcp.git
   git branch -M main
   git push -u origin main
   ```

2. **Create Streamlit Cloud Account:**
   - Visit https://share.streamlit.io
   - Sign in with GitHub

3. **Deploy:**
   - Click "New app"
   - Select your `deep-research-mcp` repository
   - Main file path: `app.py`
   - Click "Deploy"

4. **Add Secrets:**
   - Go to app settings → "Secrets"
   - Add two secrets:
     ```
     LINKUP_API_KEY=your_linkup_key
     GROQ_API_KEY=your_groq_key
     ```
   - Click "Reboot app"

5. **App is Live!** 🎉
   - Visit your public URL (shown in Streamlit Cloud dashboard)
   - Share with anyone!

#### Option B: From `groq-cloud-version/` Folder (Cloud-Optimized)

If you only want Groq (no Ollama fallback):

```bash
# Copy groq-cloud-version files to new repo root
cp groq-cloud-version/* ./
```

Then follow steps 1-5 above. This version skips Ollama checks (faster startup).

---

## 🛠️ Advanced: Using with MCP (Optional)

### What is MCP?

**Model Context Protocol (MCP)** - a standardized way for AI systems (Claude, Cursor IDE, etc.) to call your custom tools directly.

Instead of HTTP APIs, MCP exposes Python functions as callable tools that AI assistants can use natively.

**Why use MCP?**
- 🔌 **IDE Integration** - Use research tools directly in Cursor/Claude
- 🤖 **AI-Native** - Claude can decide when to run research automatically
- 🔄 **Bi-directional** - IDE tools call your Python code, results flow back
- 📚 **Context Aware** - AI understands what research tools are available and when to use them

### When to Use MCP

| Use Case | Your Setup | How It Works |
|----------|-----------|-------------|
| **Web App Only** | Streamlit (local or cloud) | Users interact via browser |
| **IDE Integration** | MCP Server + Cursor/Claude | AI assistants call research tools |
| **Both** | Streamlit + MCP together | Web app AND IDE integration |

### MCP Server Code

Your `server.py` file contains the MCP implementation:

```python
from mcp.server.fastmcp import FastMCP
from agents import run_research
import os

# Initialize the MCP Server
# "dependencies" tells the client what python libraries to install if needed
mcp = FastMCP("Deep Researcher", dependencies=["crewai", "linkup-sdk", "python-dotenv"])

@mcp.tool()
def research_topic(topic: str) -> str:
    """
    Performs deep internet research on a specific topic using AI agents.
    
    Args:
        topic: The subject to research (e.g., "Latest trends in AI 2025")
    
    Returns:
        str: Comprehensive research report with SOTA, gaps, and future work
    """
    try:
        # Ensure the key is loaded
        if not os.getenv("LINKUP_API_KEY"):
            return "Error: LINKUP_API_KEY not found in environment variables."
            
        return run_research(topic)
    except Exception as e:
        return f"Research failed: {str(e)}"

# Run the server using stdio (Standard Input/Output)
if __name__ == "__main__":
    mcp.run(transport="stdio")
```

**What This Does:**
- Exposes `research_topic()` function as a tool to MCP clients
- Any AI tool (Claude, Cursor) can call this function
- Results flow back to the AI assistant for further analysis

### Setup MCP with Cursor IDE

**Step 1: Install Cursor**
- Download from https://cursor.sh
- Install on your machine

**Step 2: Configure MCP Connection**

In Cursor, go to **Settings → Cursor Settings → Tools**

Add the MCP server configuration:

```json
{
  "mcpServers": {
    "deep-research": {
      "command": "python",
      "args": ["/absolute/path/to/deep-research-mcp/server.py"],
      "env": {
        "LINKUP_API_KEY": "your_linkup_key_here",
        "GROQ_API_KEY": "your_groq_key_here"
      }
    }
  }
}
```

**Important:** Use absolute paths, not relative paths!

**Step 3: Restart Cursor**
- Close and reopen Cursor
- Cursor will automatically start your MCP server

**Step 4: Use in Cursor**

Now in Cursor, you can ask:

```
@research-topic "quantum computing error correction approaches"
```

Or let Claude decide when to research:

```
I'm writing a paper on machine learning. Before we start, 
research the latest trends and papers from 2024-2025.
```

Cursor will automatically call your research tool!

### Setup MCP with Claude Desktop

**Step 1: Install Claude Desktop**
- Download from https://claude.ai/chat
- Install on your machine

**Step 2: Configure MCP Connection**

Create or edit `claude_desktop_config.json`:

**Windows:** `%APPDATA%\Claude\claude_desktop_config.json`
**Mac:** `~/Library/Application Support/Claude/claude_desktop_config.json`
**Linux:** `~/.config/Claude/claude_desktop_config.json`

Add:

```json
{
  "mcpServers": {
    "deep-research": {
      "command": "python",
      "args": ["/absolute/path/to/deep-research-mcp/server.py"],
      "env": {
        "LINKUP_API_KEY": "your_linkup_key_here",
        "GROQ_API_KEY": "your_groq_key_here"
      }
    }
  }
}
```

**Step 3: Restart Claude Desktop**

**Step 4: Check Tools Panel**

In Claude Desktop, you'll see a new "Tools" section:
- `research_topic` - Your research tool is now available!

Ask Claude:

```
Research quantum computing advances in 2024 and summarize the gaps in the field.
```

Claude will use your MCP-connected research tool!

### MCP + Streamlit Together

You can run **both** simultaneously:

**Terminal 1: Streamlit App**
```bash
cd local-ollama-version
streamlit run app.py
```
Opens at `http://localhost:8501`

**Terminal 2: MCP Server**
```bash
python server.py
```
Connected to Cursor/Claude

**Benefits:**
- Use web app for interactive research
- Use MCP for IDE-integrated research
- Same backend (agents.py) powers both

### Troubleshooting MCP

**Issue: "MCP Server failed to start"**
```
Solution:
1. Check absolute path is correct (not relative)
2. Ensure python in PATH: python --version
3. Install MCP dependencies: pip install mcp
4. Check .env file exists with API keys
```

**Issue: "Tool not appearing in Cursor/Claude"**
```
Solution:
1. Restart the IDE completely
2. Check server.py syntax: python server.py (should start without errors)
3. Verify paths in config are absolute, not relative
4. Check API keys are in .env file
```

**Issue: "Research returns error"**
```
Solution:
1. Same as Streamlit errors
2. Make sure LINKUP_API_KEY is set in .env
3. Test agents.py directly: python -c "from agents import run_research; print(run_research('test'))"
```

### MCP Dependencies

The MCP server requires these additional packages:

```bash
pip install mcp
pip install crewai linkup-sdk python-dotenv pydantic fpdf2
```

Or install everything:
```bash
pip install -r requirements.txt
pip install mcp
```

Note: Both `local-ollama-version/` and `groq-cloud-version/` include `mcp` in their requirements if you plan to use MCP.

---

## 📊 System Requirements

### Local Development

| Component | Minimum | Recommended |
|-----------|---------|-------------|
| Python | 3.10 | 3.11+ |
| RAM | 8GB | 16GB+ |
| Disk | 20GB | 30GB+ (for models) |
| GPU | None | NVIDIA/AMD (optional) |
| Network | 50 Mbps | 100 Mbps+ |

### Cloud Deployment

| Component | Streamlit Cloud |
|-----------|-----------------|
| RAM | Shared (1-4GB) |
| CPU | Shared |
| GPU | None (not needed) |
| Network | Automatic |
| Cost | FREE ✅ |

---

## 💰 Cost Analysis

### Local Development

| Service | Cost | Notes |
|---------|------|-------|
| Ollama | FREE | Download once, run locally |
| LinkUp API | FREE (limited) | ~100 searches/month free tier |
| Groq API | FREE (not used locally) | Fallback only |
| **Total** | **~$0** | Completely free |

### Cloud Deployment

| Service | Cost | Notes |
|---------|------|-------|
| Streamlit Cloud | FREE | Host app forever free |
| Groq API | FREE (~0.14/1M tokens) | ~$0-3/month if moderate use |
| LinkUp API | FREE (limited) | ~100 searches/month free tier |
| **Total** | **~$0-3/month** | Essentially free |

**To reduce costs further:**
- Use LinkUp free tier (100 searches/month)
- Groq free tier: 120 req/min (unlimited)
- Cache search results (future enhancement)

---

## 🔄 How Agent System Works

### The 4-Agent Pipeline

```
┌─────────────────────────┐
│ 1. Literature Reviewer  │
│                         │
│ Inputs: Research topic  │
│ Action: Search papers   │
│ Output: Paper summaries │
│         Models/Datasets │
│         Future Work     │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│ 2. Methodology Analyst  │
│                         │
│ Inputs: Search results  │
│ Action: Extract methods │
│ Output: Comparison      │
│         matrix          │
│         Metrics         │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│ 3. Gap Analyst          │
│                         │
│ Inputs: Methods matrix  │
│ Action: Identify gaps   │
│ Output: Research gaps   │
│         Contradictions  │
│         Innovations     │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│ 4. Report Writer        │
│                         │
│ Inputs: All analysis    │
│ Action: Synthesize      │
│ Output: Final report    │
│         SOTA section    │
│         Gaps section    │
│         Future work     │
└────────────┬────────────┘
             │
             ▼
         [FINAL REPORT]
```

### Agent Roles & Responsibilities

| Agent | Role | Specialization | Tools Used |
|-------|------|----------------|-----------|
| Literature Reviewer | Researcher | Searching papers | LinkUp API |
| Methodology Analyst | Data Scientist | Extracting patterns | LLM analysis |
| Gap Analyst | PhD Advisor | Strategic thinking | Reasoning models |
| Report Writer | Academic Writer | Synthesis & presentation | Language generation |

---

## 🎯 Example Usage

### Query 1: Recent AI Research

```
Topic: "Efficient attention mechanisms in transformer models"

System Flow:
├─ Search papers on efficient attention
├─ Extract: Flash Attention, Multi-Query Attention, KV-Cache
├─ Identify gap: "No attention mechanism optimizes for both speed AND memory"
└─ Report: SOTA + Gap + Future directions
```

### Query 2: Biotech Research

```
Topic: "CRISPR off-target effects and mitigation strategies"

System Flow:
├─ Search CRISPR safety papers
├─ Extract: SpCas9, PAM optimization, guideRNA design
├─ Identify gap: "Limited research on combined PAM+guideRNA optimization"
└─ Report: Current state + contradictions + new directions
```

---

## 📈 Performance Metrics

### Local Development (Ollama)

| Metric | CPU-Only | GPU (NVIDIA) |
|--------|----------|--------------|
| Search | 20s | 10s |
| Analysis | 120s | 30s |
| Report Gen | 180s | 40s |
| **Total** | **~5 min** | **~1.5 min** |

### Cloud Deployment (Groq)

| Metric | Groq Free |
|--------|-----------|
| Search | 15s |
| Analysis | 25s |
| Report Gen | 45s |
| **Total** | **~1.5 min** |

**Groq is actually faster** due to inference optimization! ⚡

---

## 🐛 Troubleshooting

### Issue: "No LLM available"

**Solution:**
```bash
# Option 1: Install Ollama
ollama pull deepseek-r1:7b

# Option 2: Add Groq API key to .env
GROQ_API_KEY=your_key_here
```

### Issue: Ollama not connecting

**Solution:**
```bash
# Make sure Ollama is running
ollama serve

# Test connection
curl http://localhost:11434/api/tags
```

### Issue: App slow on Streamlit Cloud

**Cause:** Using Groq free tier (shared resources)

**Solution:**
1. Use local development for faster iteration
2. Upgrade Groq to paid tier for production (cheap: ~$0.14 per 1M tokens)
3. Add caching to LinkUp searches

### Issue: LinkUp API returning empty results

**Solution:**
1. Check API key is valid
2. Try a different search query
3. Upgrade LinkUp plan if hitting rate limits

---

## 🚀 Future Enhancements

- [ ] Vector database for cached search results
- [ ] Batch analysis for multiple topics
- [ ] BibTeX export for academic citations
- [ ] Integration with Zotero/Mendeley
- [ ] Real-time paper feed monitoring
- [ ] Research collaboration workspace
- [ ] Custom agent creation UI
- [ ] Multi-language support

---

## 📚 Documentation

- **agents.py**: 4-agent system with detailed agent prompts
- **app.py**: Streamlit UI with session state management
- **server.py**: MCP protocol server for IDE integration
- **requirements.txt**: Minimal dependencies (6 core packages)

---

## 📄 License

MIT License - Use freely for personal or commercial projects

---

## 💬 Support

- **GitHub Issues**: Open an issue for bugs/features
- **Discussions**: Ask questions in GitHub Discussions
- **Documentation**: Check inline code comments for details

---

## 🎯 Why This Project?

✅ **Portfolio Ready** - Shows full-stack AI development  
✅ **Resume-Worthy** - Multi-agent systems, APIs, cloud deployment  
✅ **Fully Free** - No credit cards required  
✅ **Dual Deployment** - Local dev + cloud production  
✅ **Production Grade** - Error handling, logging, exports  
✅ **Educational** - Learn CrewAI, Streamlit, MCP, APIs  

---

**Built with ❤️ using Streamlit, CrewAI, Groq, and LinkUp**

Last updated: January 2, 2026

## Quick Start

### 1. Clone & Setup

```bash
git clone https://github.com/YOUR_USERNAME/deep-research-mcp.git
cd deep-research-mcp
python -m venv venv
.\venv\Scripts\activate  # Windows
# source venv/bin/activate  # Mac/Linux
pip install -r requirements.txt
```

### 2. Get Free API Keys

**LinkUp API** (required):
1. Visit https://linkup.so
2. Sign up for free
3. Copy your API key

**Groq API** (required for Streamlit Cloud, free):
1. Visit https://console.groq.com
2. Sign up (no credit card needed)
3. Copy your API key

**Ollama** (optional, for best local quality):
1. Download from https://ollama.ai
2. Run: `ollama pull deepseek-r1:7b`

### 3. Configure Environment

Create `.env` file in project root:

```
LINKUP_API_KEY=your_linkup_key_here
GROQ_API_KEY=your_groq_key_here
```

(Don't commit this file - it's in `.gitignore`)

### 4. Run Locally

```bash
streamlit run app.py
```

Opens at `http://localhost:8501`

## Usage

1. **Enter a research topic** in the text input (e.g., "quantum error correction in superconducting qubits")
2. **Wait for analysis** (takes 1-2 minutes)
3. **View research gaps** identified by the AI agents
4. **Export results** as JSON, Markdown, or PDF
5. **View history** in the sidebar

## Deploy to Streamlit Cloud (Free)

### Step 1: Push to GitHub

```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/YOUR_USERNAME/deep-research-mcp.git
git branch -M main
git push -u origin main
```

### Step 2: Deploy on Streamlit Cloud

1. Go to https://share.streamlit.io
2. Click "New app"
3. Select your GitHub repo
4. Main file path: `app.py`
5. Click "Deploy"

### Step 3: Add Secrets

In Streamlit Cloud app settings:

1. Click "Settings" → "Secrets"
2. Add:
   ```
   LINKUP_API_KEY=your_key
   GROQ_API_KEY=your_key
   ```
3. Reboot app

**Your app is now live and free!** 🎉

## How It Works

### The 4-Agent Research System

1. **Literature Reviewer Agent** - Searches for relevant papers using LinkUp
2. **Methodology Analyst Agent** - Extracts datasets, algorithms, and metrics
3. **Research Gap Analyst Agent** - Identifies unexplored combinations and gaps
4. **Report Writer Agent** - Synthesizes findings into structured reports

### Automatic LLM Selection

```
Local Development:   Ollama → DeepSeek-R1 7B (best quality)
                        ↓
Streamlit Cloud:     Groq → Mixtral 8x7B (free, fast)
```

The app auto-detects your environment and uses the best available LLM.

## Project Structure

```
deep-research-mcp/
├── app.py              # Streamlit web interface
├── agents.py           # CrewAI multi-agent system
├── server.py           # MCP protocol server (optional)
├── requirements.txt    # Python dependencies
├── .env                # Local API keys (not committed)
├── .gitignore          # Protects secrets
└── README.md           # This file
```

## Configuration

### Local Development (Best Quality)

Uses your local Ollama with DeepSeek-R1 7B. Fastest if GPU available, slower on CPU.

```bash
ollama pull deepseek-r1:7b
streamlit run app.py
```

### Streamlit Cloud (Best Deployment)

Automatically uses Groq free tier. Fast inference, completely free.

### Hybrid (Recommended)

- **Develop locally** with DeepSeek-R1 for best quality
- **Deploy to Streamlit Cloud** with Groq for free public access
- Same code works for both!

## Costs

- **LinkUp API:** Free tier (limited searches)
- **Groq API:** Free tier (120 requests/minute, unlimited)
- **Streamlit Cloud:** Free forever
- **Ollama:** Free, local only
- **Total:** $0/month if using free tiers ✅

## Troubleshooting

### "No LLM available" error
- Make sure `GROQ_API_KEY` is in `.env` (local) or Secrets (cloud)
- OR install Ollama and pull deepseek-r1:7b model

### App slow on Streamlit Cloud
- Using Groq free tier (shared resources)
- Typical response time: 30-60 seconds
- Upgrade to paid Groq tier for faster responses (~$0.14 per 1M tokens)

### Ollama not connecting
- Ensure Ollama is running: `ollama serve`
- Check it's accessible at `http://localhost:11434`

## Future Improvements

- [ ] Long-term memory with vector database
- [ ] Caching search results
- [ ] Batch analysis for multiple topics
- [ ] Export to academic formats (BibTeX, etc.)
- [ ] Integration with Zotero/Mendeley

## License

MIT License - feel free to use for personal or commercial projects

## Questions?

Open an issue on GitHub or check the documentation in the code comments.

---

**Built with ❤️ using Streamlit, CrewAI, and free APIs**
