from langchain.document_loaders.pdf import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings.bedrock import BedrockEmbeddings
from langchain.vectorstores.chroma import Chroma

def load_documents():
    document_loader = PyPDFDirectoryLoader("C:\Users\vijay\PycharmProjects\langchain_tutorial\data")
    return document_loader.load()


def split_documents(documents:list[Document]):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=80,
        length_function = len,
        is_separator_regex=False
    )
    return text_splitter.split_documents(documents)

def get_embedding_function():
    embeddings = BedrockEmbeddings(
        credentials_profile_name = "default" , region_name ="us-east-1"
    )
    return embeddings

def add_to_chroma(chunks : list[Document]):
    db = Chroma(
        persist_directory=CHROMA_PATH , embedding_function=get_embedding_function()
    )
    db.add_documents(new_chunks, ids = new_chuck_ids)
    db.persist()