# 🤖 AI YouTube Research & Blog Writer

> **A multi-agent AI system built with CrewAI that finds relevant YouTube content, extracts the relevant transcript, and transforms it into an easy-to-understand technical blog.**

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)](https://www.python.org/)
[![CrewAI](https://img.shields.io/badge/CrewAI-Multi--Agent-orange)](https://www.crewai.com/)
[![Groq](https://img.shields.io/badge/LLM-Groq%20%2B%20Qwen-purple)](https://groq.com/)
[![Hugging Face](https://img.shields.io/badge/Embeddings-HuggingFace-yellow?logo=huggingface)](https://huggingface.co/)
[![YouTube](https://img.shields.io/badge/Data-YouTube-red?logo=youtube)](https://youtube.com/)

---

## 📌 Overview

This project uses **CrewAI's multi-agent architecture** to automate the process of researching a technical topic on YouTube and converting the relevant video content into a structured blog.

Instead of manually searching through long technical videos, the system uses specialized AI agents to:

**Topic → YouTube Search → Relevant Transcript → AI Research → Technical Blog**

The current workflow uses **Krish Naik's YouTube channel** as the source for technical content and is designed around topics in **AI, Data Science, Machine Learning, and Generative AI**.

---

## ✨ Features

* 🔎 **YouTube Channel Search** — Searches a specified YouTube channel for relevant content.
* 🧠 **AI-Powered Research Agent** — Identifies the relevant video/transcript for the requested topic.
* ✍️ **AI Blog Writer Agent** — Converts the researched content into an accessible technical blog.
* 🤝 **Multi-Agent Architecture** — Separates research and writing responsibilities between specialized agents.
* ⚡ **Sequential Workflow** — Research is completed before the writing phase begins.
* 💾 **Memory & Caching** — CrewAI memory and caching are enabled to improve workflow efficiency.
* 📄 **Automatic Output** — The generated blog is saved to `output/blog.md`.
* 🚀 **Groq + Qwen** — Uses a Qwen model through Groq for the agents' language-model operations.
* 🔤 **Semantic Search Embeddings** — Uses `all-MiniLM-L6-v2` through Hugging Face for embeddings.

---

## 🏗️ Architecture

```text
                         ┌──────────────────────┐
                         │      User Topic      │
                         │   "AI vs ML vs DL"   │
                         └──────────┬───────────┘
                                    │
                                    ▼
                    ┌────────────────────────────┐
                    │       Research Agent       │
                    │                            │
                    │  • Search YouTube channel │
                    │  • Find relevant video    │
                    │  • Retrieve transcript    │
                    └──────────────┬─────────────┘
                                   │
                                   ▼
                         ┌───────────────────┐
                         │ Relevant Transcript│
                         └─────────┬─────────┘
                                   │
                                   ▼
                    ┌────────────────────────────┐
                    │        Blog Writer         │
                    │                            │
                    │ • Understand transcript    │
                    │ • Simplify concepts        │
                    │ • Generate technical blog  │
                    └──────────────┬─────────────┘
                                   │
                                   ▼
                         ┌───────────────────┐
                         │    blog.md        │
                         │  Generated Blog   │
                         └───────────────────┘
```

---

## 🧩 Agents

### 🔍 1. Blog Research Agent

The **Blog Research Agent** is responsible for finding the relevant video content for the requested topic.

Its goal is to retrieve the relevant video transcription from the configured YouTube channel. The agent is equipped with the YouTube search tool and is configured with memory and delegation capabilities.

**Responsibilities:**

* Search the configured YouTube channel.
* Identify content related to the requested topic.
* Retrieve relevant transcript information.
* Provide research material to the writing agent.

---

### ✍️ 2. Blog Writer Agent

The **Blog Writer Agent** transforms the researched video content into a readable technical blog.

It is designed to simplify complex technical concepts and present them in an engaging and accessible way.

**Responsibilities:**

* Understand the relevant transcript.
* Extract important technical concepts.
* Explain complex topics simply.
* Generate an engaging technical blog.

---

## 🛠️ Tech Stack

| Technology           | Purpose                           |
| -------------------- | --------------------------------- |
| **Python**           | Core programming language         |
| **CrewAI**           | Multi-agent orchestration         |
| **CrewAI Tools**     | YouTube channel search            |
| **Groq**             | LLM inference                     |
| **Qwen**             | Language model used by the agents |
| **Hugging Face**     | Embedding provider                |
| **all-MiniLM-L6-v2** | Semantic embedding model          |
| **python-dotenv**    | Environment variable management   |
| **YouTube**          | Source of technical video content |

---

## 📂 Project Structure

```text
.
├── agent.py          # Defines the CrewAI agents
├── crew.py           # Creates and runs the Crew
├── task.py           # Defines research and writing tasks
├── tools.py          # Configures YouTube search tool
├── output/
│   └── blog.md       # Generated blog output
└── README.md
```

### File Responsibilities

**`agent.py`**

Contains the two agents:

* `blog_research`
* `blog_writer`

The agents use the Qwen model through Groq and the configured YouTube tool.
**`task.py`**

Defines the two sequential tasks:

1. Find the relevant video transcript.
2. Generate a blog from that transcript.

Both tasks write their result to `output/blog.md`.

**`tools.py`**

Configures `YoutubeChannelSearchTool` for the `@krishnaik06` channel and uses Qwen through Groq with `all-MiniLM-L6-v2` embeddings.

**`crew.py`**

Creates the CrewAI workflow with:

* 2 agents
* 2 tasks
* Sequential processing
* Memory enabled
* Caching enabled
* `max_rpm=100`

The current example runs the workflow with the topic **`AI VS ML VS DL`**.

---

## ⚙️ How the Workflow Works

### Step 1 — Provide a Topic

The workflow accepts a topic such as:

```python
inputs = {
    "topic": "AI VS ML VS DL"
}
```

### Step 2 — Search YouTube

The research agent uses the configured YouTube channel search tool to locate relevant content.

### Step 3 — Research

The **Blog Research Agent** retrieves the relevant transcript for the selected topic.

### Step 4 — Generate the Blog

The transcript is passed through the workflow to the **Blog Writer Agent**, which generates the final article.

### Step 5 — Save Output

The final blog is written to:

```text
output/blog.md
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/<your-repository>.git
cd <your-repository>
```

### 2. Install dependencies

Install the Python packages required by the project:

```bash
pip install crewai crewai-tools langchain-groq python-dotenv
```

### 3. Configure environment variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

The project loads environment variables using `python-dotenv` and accesses the Groq API key through `GROQ_API_KEY`.

### 4. Run the project

```bash
python crew.py
```

The generated result is written to:

```text
output/blog.md
```

---

## 🧪 Example

### Input

```text
AI VS ML VS DL
```

### Workflow

```text
AI VS ML VS DL
      ↓
YouTube Channel Search
      ↓
Relevant Video
      ↓
Transcript
      ↓
Research Agent
      ↓
Blog Writer Agent
      ↓
output/blog.md
```

---

## 🔐 Environment Variables

| Variable       | Description                        |
| -------------- | ---------------------------------- |
| `GROQ_API_KEY` | API key used for Groq model access |

> **Never commit your `.env` file or API keys to GitHub.**

Add this to `.gitignore`:

```gitignore
.env
__pycache__/
*.pyc
output/
```

---

## 🎯 Why Multi-Agent?

A major idea behind this project is **specialization**.

Instead of asking one general-purpose agent to perform the entire workflow, the system divides the work:

```text
Research Agent
      │
      ▼
Find + Understand Source
      │
      ▼
Writer Agent
      │
      ▼
Create Final Content
```

This separation makes each agent responsible for a clear objective and demonstrates how **agentic workflows can coordinate multiple specialized AI roles**.

---

## 🔮 Future Improvements

Potential extensions for the project include:

* 🌐 Support for multiple YouTube channels.
* 📚 Research across multiple videos instead of a single source.
* 🔗 Add source links and citations to generated blogs.
* 🧠 Add a dedicated fact-checking agent.
* 📝 Add SEO optimization for generated articles.
* 📊 Add topic classification before research.
* 💬 Add an interactive CLI or web interface.
* 📄 Export blogs to PDF or HTML.
* 🔄 Add a critic/reviewer agent for quality control.

---

## 📚 Concepts Demonstrated

This project is a practical example of:

* **Agentic AI**
* **Multi-Agent Systems**
* **CrewAI**
* **Task Orchestration**
* **Tool Calling**
* **LLM-based Research**
* **Semantic Search**
* **Embeddings**
* **Prompt-driven Agents**
* **Sequential Agent Workflows**
* **Generative AI Content Creation**

---

## 👨‍💻 Author

**Pranshu Awasthy**

Built as a hands-on project while learning **Generative AI, Agentic AI, CrewAI, LLMs, and RAG-related technologies**.

---

## ⭐ Support

If you found this project useful, consider giving the repository a ⭐ on GitHub.

---

> **Built with Python + CrewAI + Groq + Qwen + YouTube + Hugging Face**
