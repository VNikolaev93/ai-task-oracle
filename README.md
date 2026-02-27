# 🤖 AI Task Oracle (Multi-Agent Task Extractor)

A professional AI-powered tool designed to transform unstructured meeting notes into structured project tasks using a **Multi-Agent Reflection Pattern**.

## 🚀 Overview
Extracting actionable tasks from messy meeting transcripts is a common business pain point. This tool solves it by using **Llama 3.3 (70B)** to identify tasks, assignees, and deadlines with high logical accuracy.

## 🛠 Key Engineering Features
- **Multi-Agent Workflow:** Implements a "Draft & Critique" pattern where a second AI agent validates the first agent's output to prevent hallucinations and logic errors.
- **Date Reasoning:** Automatically calculates relative deadlines (e.g., "next Friday" or "within 3 days") based on the meeting date.
- **SOTA LLM Integration:** Powered by Llama 3.3 via **Groq API** for sub-second inference speeds.
- **Interactive Web UI:** Built with **Streamlit** for seamless document uploads and data visualization.
- **Business Export:** Outputs data in structured JSON and CSV (Excel-compatible) formats.

## 🧰 Tech Stack
- **Language:** Python 3.10+
- **LLM Orchestration:** LangChain
- **Models:** Llama-3.3-70b-versatile
- **API Provider:** Groq
- **Frontend:** Streamlit
- **Data Handling:** Pandas, JSON, CSV

## 📂 Project Structure
- `ui.py`: Streamlit web interface logic.
- `core.py`: Multi-agent LLM logic and prompts.
- `config.py`: Environment configuration and model settings.
- `meeting_notes.txt`: Example input for testing.

## 🔧 Installation & Setup
1. Clone the repository: `git clone <your-repo-link>`
2. Install dependencies: `pip install -r requirements.txt`
3. Create a `.env` file and add your key: `GROQ_API_KEY=your_key_here`
4. Run the app: `streamlit run ui.py`

---
*Developed by Viacheslav Nikolaev | QA to AI Engineer Journey 2026*