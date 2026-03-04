# 🕵️ AI Research Agent

An autonomous AI agent that searches the web, reasons across multiple sources, and delivers detailed answers to any question — all in real time.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.54-red)
![Groq](https://img.shields.io/badge/Groq-GPT--OSS--120b-orange)
![Tavily](https://img.shields.io/badge/Tavily-Search%20API-green)

![AI-AGENT](https://github.com/user-attachments/assets/c6d6ac06-9fa4-4e6e-acf3-3f036cfe938e)

---

## 🚀 Demo

1. Type any question into the chat
2. The agent autonomously decides to search the web
3. It reads and reasons across multiple sources
4. You get a detailed, synthesized answer in seconds

Example questions:
- *"What are the biggest AI breakthroughs in 2025?"*
- *"Compare the latest LLM models available today"*
- *"What is the latest news about OpenAI?"*

---

## 🧠 How It Works

This project implements a **ReAct (Reason + Act)** agentic loop:

```
Question
   ↓
THINK — What do I need to find to answer this?
   ↓
ACT — Call web_search tool with a query
   ↓
OBSERVE — Read the search results
   ↓
THINK — Do I have enough info?
   ↓
ACT again if needed / ANSWER when ready
```

The agent keeps looping autonomously until it has enough information to give a confident answer — without any hardcoded steps.

---

## 🛠 Tech Stack

| Tool | Purpose |
|------|---------|
| **Streamlit** | Frontend chat UI |
| **Groq** | LLM inference (fast & free) |
| **GPT-OSS-120b** | The reasoning model powering the agent |
| **Tavily Search API** | Real-time web search tool |
| **Python 3.11** | Core language |

---

## ⚙️ Setup & Installation

### 1. Clone the repo
```bash
git clone https://github.com/Rafay1802/ai-research-agent.git
cd ai-research-agent
```

### 2. Create a virtual environment
```bash
python3.11 -m venv venv
source venv/bin/activate  # Mac/Linux
```

### 3. Install dependencies
```bash
pip install streamlit groq tavily-python python-dotenv
```

### 4. Set up environment variables
Create a `.env` file in the root directory:
```
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
```

### 5. Run the app
```bash
streamlit run app.py
```

Open your browser at `http://localhost:8501`

---

## 📁 Project Structure

```
ai-research-agent/
├── app.py                  # Streamlit UI
├── agent/
│   ├── tools.py            # Web search tool definition
│   └── graph.py            # Agentic ReAct loop
├── .env                    # API keys (not committed)
├── .gitignore
└── README.md
```

---

## 🔑 Getting API Keys

- **Groq** (free) → [console.groq.com](https://console.groq.com)
- **Tavily** (free tier) → [app.tavily.com](https://app.tavily.com)

---

## 💡 What Makes This Different from a Regular Chatbot

A regular chatbot answers from its training data — it can't access the internet and its knowledge has a cutoff date.

This agent:
- 🔍 Searches the web in real time
- 🔄 Reasons in a loop — decides its own next steps
- 📚 Synthesizes multiple sources into one answer
- 🧠 Knows when it has enough information to stop searching

This is the architecture used in production AI systems at companies like Perplexity, You.com, and countless AI startups.

---

## 📄 License

MIT License — feel free to use and modify.
