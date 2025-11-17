import chromadb # for vector db
import re # for text cleaning
from langchain_ollama import OllamaEmbeddings
from nltk.tokenize import word_tokenize # for chunking
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_chroma import Chroma
from langchain.chains import RetrievalQA
import ollama

#### PDF READER ####
# start by extracting text from the pdf for the GPS guide
loader = PyMuPDFLoader("example.pdf")
docs = loader.load()


#### TEXT CLEANING ####
# text cleaning
def clean_text(text):
    text = re.sub(r'\s+', ' ', text)  
    text = re.sub(r'[^\x00-\x7F]+', ' ', text)  
    return text.strip()

#### DATA CHUNKING ####

# chunk data

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,  # number of characters per chunk
    chunk_overlap=100,  # overlap between chunks
    length_function=len,
    separators=["\n\n", "\n", " ", ""]  # try to split on paragraphs/sentences first
)

# calling the text splitting method
split_docs = text_splitter.split_documents(docs)

#### VECTOR DATABASE CREATION ####

embeddings = OllamaEmbeddings(model="nomic-embed-text")

# store split document and embeddings in chroma database
db = Chroma.from_documents(
    split_docs, 
    embeddings, 
    persist_directory="./my_chroma_db_langchain"
)

# writes to folder

db.persist() 

retriever = db.as_retriever(search_kwargs={"k": 3})

##### set up local model ######

llm = ollama(model="llama3.2")

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    return_source_documents=True
)

query = "What does the GPS guide say about waypoint accuracy?"
response = qa_chain({"query": query})

print("Answer:", response["result"])
print("\nSources used:")
for doc in response["source_documents"]:
    print("-", doc.metadata)
