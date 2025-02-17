# **AI-Powered Data Retrieval System**

**Project Overview**

This project implements an AI-powered data retrieval system using LLMs (Large Language Models), RAG (Retrieval-Augmented Generation), and a vector database. Users can search for information in a dataset using natural language queries, and the system will retrieve relevant documents and generate AI-powered responses.

**Features**

1. Converts text data into vector embeddings for efficient searching.
2. Stores and retrieves embeddings using FAISS (Facebook AI Similarity Search).
3. Uses OpenAI's GPT-4 or other LLMs to generate intelligent responses.
4. Provides an API endpoint for querying the system.
5. Deployable on Flask, FastAPI, AWS Lambda, or Hugging Face Spaces.

**Tech Stack**
1. Python
2. FAISS for vector storage
3. LangChain for RAG implementation
4. Sentence-Transformers for text embeddings
5. OpenAI API for LLM-powered responses
6. Flask/FastAPI for serving as an API

### **Setup and Installation**

1. Clone the Repository

git clone https://github.com/yourusername/ai-data-retrieval.git
cd ai-data-retrieval

2. Install Dependencies

pip install -r requirements.txt

3. Set Up OpenAI API Key

Obtain an API key from OpenAI and set it in your environment:

export OPENAI_API_KEY="your-api-key"

4. Run the Application

python app.py

5. Test the API

Send a query using curl:

curl -X POST "http://127.0.0.1:5000/search" -H "Content-Type: application/json" -d '{"query": "What is AI?"}'

Future Enhancements

Add UI using Streamlit

Support multiple data sources (PDFs, SQL databases)

Use alternative LLMs (Mistral, Claude, Llama)

Improve retrieval ranking using hybrid search

License

This project is licensed under the MIT License.