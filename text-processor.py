import chromadb # for vector db
import fitz # for pdf reading
import re # for text cleaning
from nltk.tokenize import word_tokenize # for chunking
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyMuPDFLoader


# start by extracting text from the pdf for the GPS guide
loader = PyMuPDFLoader("example.pdf")
docs = loader.load()

# text cleaning
def clean_text(text):
    text = re.sub(r'\s+', ' ', text)  
    text = re.sub(r'[^\x00-\x7F]+', ' ', text)  
    return text.strip()

# chunk data

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,  # number of characters per chunk
    chunk_overlap=100,  # overlap between chunks
    length_function=len,
    separators=["\n\n", "\n", " ", ""]  # try to split on paragraphs/sentences first
)

# calling the text splitting method
split_docs = text_splitter.split_documents(docs)

