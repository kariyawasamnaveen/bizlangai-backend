# app/services/knowledge_service.py
import os
from langchain_community.document_loaders import PyPDFLoader, UnstructuredWordDocumentLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_mongodb import MongoDBAtlasVectorSearch
from app.db.database import client

class KnowledgeService:
    def __init__(self):
        self.embeddings = OpenAIEmbeddings()
        self.db_name = "bizlangai_db"
        self.collection_name = "knowledge_base"
        self.collection = client[self.db_name][self.collection_name]
        self.vector_search_index_name = "vector_index"

    def process_file(self, file_path: str, file_type: str):
        """Processes a file and stores its embeddings in MongoDB Atlas."""
        
        # 1. Load Document
        if file_type == "pdf":
            loader = PyPDFLoader(file_path)
        elif file_type == "docx":
            loader = UnstructuredWordDocumentLoader(file_path)
        else:
            loader = TextLoader(file_path)
            
        docs = loader.load()
        
        # 2. Split Document into chunks
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
        splits = text_splitter.split_documents(docs)
        
        # 3. Store in MongoDB Vector Search
        MongoDBAtlasVectorSearch.from_documents(
            documents=splits,
            embedding=self.embeddings,
            collection=self.collection,
            index_name=self.vector_search_index_name
        )
        
        return f"✅ Successfully indexed {len(splits)} chunks from {os.path.basename(file_path)}"

    def get_retriever(self):
        """Returns a retriever for the knowledge base."""
        vector_search = MongoDBAtlasVectorSearch(
            collection=self.collection,
            embedding=self.embeddings,
            index_name=self.vector_search_index_name
        )
        return vector_search.as_retriever(search_type="similarity", search_kwargs={"k": 5})

knowledge_service = KnowledgeService()
