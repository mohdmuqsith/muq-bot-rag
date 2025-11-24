import streamlit as st  
from dotenv import load_dotenv
import os
from utils import (
    load_files,
    create_vector_store,
    hash_files,
    load_cache,
    save_cache,
    make_rdf_triples,
    owl_relation,
    compute_similarity_scores
)

from langchain_google_genai import ChatGoogleGenerativeAI


# ---------------- CONFIG ---------------- #
load_dotenv(".env")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
st.set_page_config(page_title="MuqBOT", layout="wide")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


# ---------------- LLM ---------------- #
llm = ChatGoogleGenerativeAI(
    model="models/gemini-2.5-flash",
    temperature=0.0,
    google_api_key=GOOGLE_API_KEY
)


# ---------------- SIDEBAR ---------------- #
st.sidebar.header("Upload Documents")

uploaded_files = st.sidebar.file_uploader(
    "Upload PPTX, PDF, DOCX",
    type=["pptx", "pdf", "docx"],
    accept_multiple_files=True
)

if st.sidebar.button("Build / Load Knowledge Base"):
    if not uploaded_files:
        st.sidebar.error("Upload at least one file!")
    else:
        files_hash = hash_files(uploaded_files)
        st.session_state["files_hash"] = files_hash

        cached = load_cache(files_hash)
        if cached:
            st.session_state.vector_db = cached
            st.sidebar.success("Loaded from Cache")
        else:
            with st.spinner("Extracting text & creating embeddings..."):
                text = load_files(uploaded_files)
                vector_db = create_vector_store(text)
                save_cache(files_hash, vector_db)
                st.session_state.vector_db = vector_db

            st.sidebar.success("Knowledge Base Ready")


# ---------------- MAIN UI ---------------- #
st.title("🔎 MuqBOT — RDF • Similarity")


query = st.text_input("Ask something:")
ask = st.button("Ask")


if ask and query:
    if "vector_db" not in st.session_state:
        st.error("Upload documents and build the knowledge base first.")
    else:
        docs = st.session_state.vector_db.similarity_search(query, k=4)

        context = "\n\n".join([d.page_content for d in docs])

        prompt = f"""
        Use ONLY the provided context.
        If answer is not found, reply: "I don't know".

        Context:
        {context}

        Question:
        {query}
        """

        response = llm.invoke(prompt)
        answer = response.content

        st.session_state.chat_history.append(("You", query))
        st.session_state.chat_history.append(("Bot", answer))

        st.subheader("Answer")
        st.write(answer)

        # ---------- semantic extras ----------- #
        st.subheader("RDF Triples : ")
        for d in docs:
            triples = make_rdf_triples(d.page_content)
            for s, p, o in triples:
                st.write(f" • ({s}, {p}, {o})")

        #st.subheader("🦉 OWL-Style Relations (Demo)")
        #st.write(owl_relation("MedicalTerm", "isRelatedTo", "OntologyConcept"))

        st.subheader("📊 Semantic Similarity Scores")
        embedder = st.session_state.vector_db.embedding_function
        scores = compute_similarity_scores(query, docs, embedder)

        for doc, sc in zip(docs, scores):
            st.write(f"Score: {sc:.4f}")
            st.caption(doc.page_content[:180] + "...")

        st.divider()


# ---------------- CHAT HISTORY ---------------- #
st.subheader("Chat History")

for role, msg in st.session_state.chat_history:
    if role == "You":
        st.markdown(f"**🧑 You:** {msg}")
    else:
        st.markdown(f"**🤖 MuqBOT:** {msg}")


