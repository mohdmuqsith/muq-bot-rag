# Semantic RAG Chatbot

A Retrieval-Augmented Generation (RAG) chatbot built with **Streamlit**, **FAISS**, **HuggingFace embeddings**, and **Google Gemini**.  
It allows users to upload documents, perform semantic search, and generate accurate, context-aware answers using large language models.

This project also demonstrates **RDF-like semantic triple extraction**, **semantic similarity scoring**, and is inspired by research on **LLM-powered intelligent knowledge graph construction** in medical domains.

---

## 🚀 Features

- Upload multiple documents
- Extract text from **PDF / PPTX / DOCX**
- Smart text chunking using `RecursiveCharacterTextSplitter`
- Vector embeddings with **all-MiniLM-L6-v2**
- High-speed semantic search using **FAISS**
- **Google Gemini** for answer generation
- Auto-generated **semantic triples** (demo)
- Semantic similarity scoring
- Vector store caching for fast reloads
- Fully interactive **Streamlit UI**

---

## 🧠 Tech Stack

- Python 3.10+
- Streamlit
- LangChain
- FAISS
- sentence-transformers
- Google Generative AI (Gemini)

---

## 📁 Project Structure

```
Logic_Demo/
│
├── app.py            # Main Streamlit application
├── utils.py          # Loaders, chunking, FAISS helpers
├── test.py           # Gemini API test script
├── requirements.txt # Dependencies
└── README.md         # Project documentation
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/mohdmuqsith/muq-bot-rag.git
cd muq-bot-rag
```

---

### 2. Create a Virtual Environment

**Windows**
```bash
python -m venv venv
venv\Scripts\activate
```

**Mac / Linux**
```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Setting Up API Keys

### Option 1: Streamlit Secrets (Recommended)

Create the file:

```
.streamlit/secrets.toml
```

Add:

```
GOOGLE_API_KEY = "your_api_key_here"
```

---

### Option 2: Environment Variable

**Windows**
```bash
setx GOOGLE_API_KEY "your_api_key_here"
```

**Mac / Linux**
```bash
export GOOGLE_API_KEY="your_api_key_here"
```

---

## ▶️ Running the App

```bash
streamlit run app.py
```

Open in your browser:

```
http://localhost:8501
```

---

## 🔍 How It Works

1. User uploads documents  
2. Text is extracted  
3. Text is chunked  
4. Chunks are embedded using HuggingFace  
5. Embeddings are stored in FAISS  
6. User asks a question  
7. Top-k relevant chunks are retrieved  
8. Gemini generates the final answer  
9. Semantic triples & similarity scores are displayed  

---

## ✅ Testing Your Gemini API Key

Use the built-in test script:

```bash
python test.py
```

This confirms that your API key and model access are working.

---

## ☁️ Deployment (Streamlit Cloud)

1. Push your repository to GitHub  
2. Visit: https://share.streamlit.io  
3. Connect your repository  
4. Select `app.py`  
5. Add the following in **Secrets**:

```
GOOGLE_API_KEY = "your_api_key_here"
```

6. Deploy 🚀

---

## 🛠 Troubleshooting

### ❌ Model not found (404)
Your Gemini account may not support the chosen model.  
Use `test.py` to list available models.

---

### ❌ FAISS import issues
Install the CPU-only version:

```bash
pip install faiss-cpu
```

---

### ❌ Streamlit secrets error
Make sure:
- `.streamlit/secrets.toml` exists  
- It is correctly indented  
- No extra spaces or quotes  

---

## 📄 License

MIT License

---

## 🙏 Credits

Inspired by research on **LLM-assisted RDF knowledge graph construction**, **semantic retrieval workflows**, and medical ontology mapping using large language models.

Research Inspiration:
- *Large Language Models for Intelligent RDF Knowledge Graph Construction*
- Published in **Frontiers in Artificial Intelligence (2025)**
- Focus: Medical ontology mapping, semantic interoperability, and explainable AI

---

## 👤 Author

**Mohammed Abdul Muqsith**  
Demo Project: https://github.com/mohdmuqsith/muq-bot-rag.git  









