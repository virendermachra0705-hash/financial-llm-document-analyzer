import streamlit as st
from document_loader import load_document, split_documents
from vector_store import create_vector_store
from rag_pipeline import create_rag_chain

st.title("AI Financial Document Analyzer")

uploaded_file = st.file_uploader("Upload Financial Document", type=["pdf"])

if uploaded_file:

    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())

    # 1 Load document
    documents = load_document("temp.pdf")

    # 2 Chunk document
    chunks = split_documents(documents)

    # 3 Create vector database
    vectorstore = create_vector_store(chunks)

    # 4 Create RAG pipeline
    qa_chain = create_rag_chain(vectorstore)

    question = st.text_input("Ask a question about the document")

    if question:
        answer = qa_chain.invoke({"query": question})
        st.write(answer)

analysis_button = st.button("Analyze Document")

if analysis_button:

    analysis_query = """
    Extract claim amount, policy type, incident type, risk level and recommendation.
    """

    result = qa_chain.invoke({"query": analysis_query})

    answer = result["result"]

    st.subheader("AI Document Analysis")
    st.write(answer)

summary_button = st.button("Generate Document Summary")

if summary_button:

    summary_query = "Provide a concise summary of this document."

    result = qa_chain.invoke({"query": summary_query})

    summary = result["result"]

    st.subheader("Document Summary")
    st.write(summary)