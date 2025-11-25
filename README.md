Semantic RAG Chatbot

A Retrieval-Augmented Generation (RAG) based chatbot built with Streamlit, FAISS, HuggingFace embeddings, and Google Gemini.
It allows you to upload documents (PDF, PPTX, DOCX), extract text, embed it, store it in a vector database, retrieve relevant chunks, and generate LLM-powered answers.
The app also demonstrates simple RDF-like triple extraction and semantic similarity scoring.

Features

Upload multiple documents

Extract text from PDF / PPTX / DOCX

Chunking using RecursiveCharacterTextSplitter

Vector embeddings via HuggingFace (all-MiniLM-L6-v2)

Vector search using FAISS

Google Gemini for answer generation

Auto-generated semantic triples (demo)

Semantic similarity scoring

Vector store caching for fast reload

Fully interactive Streamlit UI

Tech Stack

Python 3.10+

Streamlit

LangChain

FAISS

sentence-transformers

Google Generative AI (Gemini)

Project Structure
Logic_Demo/
│
├── app.py                 # Streamlit application
├── utils.py               # Helper functions (loaders, FAISS, chunking, etc.)
├── test.py                # Script to test Gemini API
├── requirements.txt       # Dependencies
└── README.md              # This file

Installation
1. Clone the repository
git clone https://github.com/<your-username>/Logic_Demo.git
cd Logic_Demo

2. Create a virtual environment

Windows:

python -m venv venv
venv\Scripts\activate


Mac/Linux:

python3 -m venv venv
source venv/bin/activate

3. Install dependencies
pip install -r requirements.txt

Setting up API Keys

Create:

.streamlit/secrets.toml


Add:

GOOGLE_API_KEY = "your_api_key_here"


Alternatively, set environment variable:

Windows:

setx GOOGLE_API_KEY "your_api_key_here"


Linux/Mac:

export GOOGLE_API_KEY="your_api_key_here"

Running the App
streamlit run app.py


Then open:

http://localhost:8501

How It Works

Upload documents

The system extracts text from each file

Text is chunked

Each chunk is embedded using a HuggingFace model

Embeddings stored in FAISS vector DB

User asks a question

System retrieves top-k relevant chunks

Gemini uses those chunks as context to answer

Semantic triples + similarity scores are displayed

Testing Your Gemini API Key

test.py includes a minimal script to confirm your API key works:

python test.py

Deployment
Deploy to Streamlit Cloud

Push repo to GitHub

Visit: https://share.streamlit.io

Connect your repo → select app.py

Add secrets in App Settings → Secrets:

GOOGLE_API_KEY = "your_api_key_here"


Deploy

Troubleshooting

Model not found error (404)
Your Gemini account may not support the model name.
Use the test script to list supported models.

FAISS import issues
Install CPU-only FAISS:

pip install faiss-cpu


Streamlit secret errors
Ensure .streamlit/secrets.toml exists and is properly indented.

License

MIT License

Credits

Inspired by research on LLM-assisted RDF Knowledge Graph construction and semantic retrieval workflows.
