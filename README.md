# AI Financial Document Analyzer (LLM + RAG)

This project is an AI-powered document analysis system that uses Large Language Models (LLMs) and Retrieval Augmented Generation (RAG) to analyze financial documents such as insurance claims and policy documents.

## Features

- Upload financial documents (PDF)
- Ask questions about documents
- Automatic document summary
- AI-based risk analysis
- Claim detail extraction

## Tech Stack

- Python
- Streamlit
- LangChain
- FAISS Vector Database
- HuggingFace Embeddings
- Llama3 via Ollama

## Architecture

PDF Upload  
↓  
Document Loader  
↓  
Text Chunking  
↓  
Embedding Generation  
↓  
FAISS Vector Database  
↓  
Retriever  
↓  
LLM (Llama3)  
↓  
Answer / Risk Analysis

## Installation

```bash
git clone https://github.com/YOUR_USERNAME/financial-llm-document-analyzer.git
cd financial-llm-document-analyzer
pip install -r requirements.txt