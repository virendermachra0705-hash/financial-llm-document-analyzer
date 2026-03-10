from langchain.llms import Ollama
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate


def create_rag_chain(vectorstore):

    llm = Ollama(model="llama3")

    retriever = vectorstore.as_retriever()

    prompt_template = """
You are a financial risk analyst.

Analyze the provided insurance or financial document and extract the following:

1. Claim Amount
2. Policy Type
3. Incident Type
4. Risk Level (Low / Medium / High)
5. Recommendation (Approve / Investigate / Reject)

Use only the information from the document context.

Context:
{context}

Question:
{question}

Answer:
"""

    PROMPT = PromptTemplate(
        template=prompt_template,
        input_variables=["context", "question"]
    )

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type_kwargs={"prompt": PROMPT}
    )

    return qa_chain