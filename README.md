# math-professor-agent
# 🧮 Math Professor Agent

A fully functional **Agentic RAG system** that acts like a math professor:  
Ask it any math question — it searches a knowledge base and responds with step-by-step solutions using LLMs.

---

## 🚀 Live Demo
👉 [Try it on Streamlit](https://your-deployed-app-link.streamlit.app)

---

## 📂 Project Structure

```bash
math-professor-agent/
├── app.py                    # Main Streamlit app
├── config.py                 # Loads .env credentials
├── requirements.txt          # All dependencies
├── .env.example              # Sample environment config (no secrets)
│
├── agents/
│   ├── kb_agent.py           # Searches knowledge base
│   ├── web_agent.py          # Web fallback agent (optional)
│   └── feedback_agent.py     # Human feedback support
│
├── services/
│   ├── vector_store.py       # Weaviate upload/search logic
│   ├── embedding_service.py  # HuggingFace/OpenAI embedding
│   └── search_service.py     # Web search fallback (Tavily)
│
├── utils/
│   ├── guardrails.py         # Guardrails / safety (optional)
│   └── logger.py             # Logging utility
│
└── data/
    └── parsed_math_knowledge.json   # Your knowledge base

---

## ⚙️ Setup Instructions

### 1. Clone this repo

```bash
git clone https://github.com/Saichandra30/math-professor-agent.git
cd math-professor-agent
pip install -r requirements.txt
WEAVIATE_ENDPOINT=https://your-weaviate-endpoint
WEAVIATE_API_KEY=your-api-key
python setup_kb.py
python -m agents.kb_agent
✅ Example Usage
vbnet
Copy code
User: What is the derivative of x²?
Agent: ✅ Step-by-step solution: The derivative of x² is 2x.
📊 Future Work
Add JEE Benchmark Dataset

Add feedback_agent and web_agent integration

Expand knowledge base to support scanned math PDFs

💡 Future Work
Integrate scanned PDF → JSON ingestion

Web Search agent fallback via Tavily

Benchmarking on JEE or MATHQA datasets

Gradio / Streamlit UI for public access




