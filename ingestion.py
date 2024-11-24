from langchain_core.documents import Document
import json
from dotenv import load_dotenv
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

load_dotenv()

# dream_data.json dosyasını okuma
with open('/Users/kardelruveyda/Desktop/MyProjects/langgraph-mystic/mystic/dream_data.json', 'r') as file:
    dream_data = json.load(file)

# JSON verilerini Document nesnelerine dönüştürme
documents = [
    Document(
        page_content=dream["page_content"],  # 'page_content' alanını alıyoruz
        metadata=dream["metadata"]  # 'metadata' alanını alıyoruz
    )
    for dream in dream_data["dreams"]
]

vectorstore = Chroma.from_documents(
    documents,
    collection_name="rag-chroma",
    embedding=OpenAIEmbeddings(),
    # veri tabanının harddiske kaydedildiği ve onun üzerindien okunabildiği ortama çeviriyoruz
    persist_directory='./.chroma'
)

retriever = Chroma(
        collection_name="rag-chroma",
        persist_directory='./.chroma',
        embedding_function=OpenAIEmbeddings(),
).as_retriever()

