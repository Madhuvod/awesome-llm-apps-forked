import streamlit as st
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaEmbeddings
from langchain_ollama import ChatOllama

st.title("Chat with Webpage 🌐")
st.caption("This app allows you to chat with a webpage using local llama3 and RAG")

# Get the webpage URL from the user
webpage_url = st.text_input("Enter Webpage URL", type="default")
# Connect to Ollama
ollama_endpoint = "http://127.0.0.1:11434"
ollama_model = "llama3.1"
ollama = ChatOllama(model=ollama_model, base_url=ollama_endpoint)

if webpage_url:
    # 1. Load the data
    loader = WebBaseLoader(webpage_url)
    docs = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=10)
    splits = text_splitter.split_documents(docs)

    # 2. Create Ollama embeddings and vector store
    embeddings = OllamaEmbeddings(model=ollama_model, base_url=ollama_endpoint)
    vectorstore = Chroma.from_documents(documents=splits, embedding=embeddings)

    # 3. Call Ollama Llama3 model
    def ollama_llm(question, context):
        """Generates a response to a question using the Ollama Llama3 model.

    This function takes a question and its context, formats them into a prompt, 
    and invokes the Ollama Llama3 model to generate a response.

    Args:
        question (str): The question to be answered by the model.
        context (str): The context or additional information related to the question.

    Returns:
        str: The response generated by the Ollama Llama3 model, stripped of leading and trailing whitespace."""
        formatted_prompt = f"Question: {question}\n\nContext: {context}"
        response = ollama.invoke([('human', formatted_prompt)])
        return response.content.strip()

    # 4. RAG Setup
    retriever = vectorstore.as_retriever()

    def combine_docs(docs):
        """Combines the content of multiple document objects into a single string.

    Args:
        docs (list): A list of document objects, each having a 'page_content' attribute.

    Returns:
        str: A string consisting of the combined 'page_content' of all document objects,
        separated by two newline characters."""
        return "\n\n".join(doc.page_content for doc in docs)

    def rag_chain(question):
        """Processes a question to retrieve and format relevant documents, and generates a response using a language model.

    Args:
        question (str): The question or query that needs to be answered.

    Returns:
        str: The response generated by the language model based on the retrieved and formatted documents."""
        retrieved_docs = retriever.invoke(question)
        formatted_context = combine_docs(retrieved_docs)
        return ollama_llm(question, formatted_context)

    st.success(f"Loaded {webpage_url} successfully!")

    # Ask a question about the webpage
    prompt = st.text_input("Ask any question about the webpage")

    # Chat with the webpage
    if prompt:
        result = rag_chain(prompt)
        st.write(result)
