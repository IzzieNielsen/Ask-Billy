# Ask-Billy - A Creighton Student Chatbot

## Overview
Chatbot to answer questions about Creighton for students. RAG model trained on data from the RSP binder, which serves as a guide for new students. The model will be implemented using Python and and a local Ollama LLM.

## Features
* Simple and easy to use streamlit frontend
* Ollama 3.2 local LLM to protect Creighton data
* Langchain vector database to store document embeddings
* RAG implementation to reduce hallucinations for this specialized chatbot
* Ability to answer common questions for new Creighton students
* Redirects questions that fall outside of the source material
* Stores chat data for better coversations

## Installation

### Prerequisites

* Python 3.8+
* Required packages

### Setup

1. Clone git repository
```bash
git clone https://github.com/IzzieNielsen/Ask-Billy
cd Ask-Billy
```
2. Install all dependencies
```bash
pip3 install -r requirements.txt
```
3. Place data files in directory
     * Binder.pdf
4. Run program in terminal
```bash
streamlit run app.py
```
5. Access the application
     * Open browser to http://localhost:8501
     * Model may take a few minutes to compile (<5 minutes)
     * Start asking questions!
  
## File Structure
```bash
.
├── __pycache__                                    # stored chat history
│   └── text_processor.cpython-312.pyc
├── app.py                                         # main application
├── Binder.pdf                                     # data used by RAG
├── creightonlogo.png                              # image in frontend
├── my_chroma_db_langchain                         # vector database
│   ├── 46916de7-39d2-4a5c-98fc-905c7984d152
│   │   ├── data_level0.bin
│   │   ├── header.bin
│   │   ├── index_metadata.pickle
│   │   ├── length.bin
│   │   └── link_lists.bin
│   ├── chroma.sqlite3
│   └── f32709ec-efc5-4d1d-8427-27c46d71211e
│       ├── data_level0.bin
│       ├── header.bin
│       ├── index_metadata.pickle
│       ├── length.bin
│       └── link_lists.bin
├── rag-chatbot            
│   └── src
│       └── main.py                               # text processing file
├── README.md                                     # this file
└── requirements.txt                              # required libraries
```

## Technical Details

### Data Processing
* **PDF Reader:** uses langchain PyMuPDFLoader to process the RSP Binder
* **Text Cleaning:** removes ASCII character, sequences of one or more whitespace characters, and leading or trailing whitespaces
* **Chunks:** creates chunks around 1,000 characters long with around 100 characters of overlap to preserve context
        * Tries to break at natural boundaries first 
  
### Embedding and Vector DB
* **Embedding Method:** nomic-embed-text from Ollama to transform chunks into numerical vectors
* **Database:** stores vector embeddings, metadata, and chunk text into the langchain chroma db

### Model Creation
* **Model:** Ollama 3.2 for robust performance and small size to run quickly locally
* **Location:** model runs locally for data privacy

### Frontend
* **Streamlit:** library for simple chatbot design
* **App.py:** contains model frontend information
* **Query Entry:** textbox for query input

## Authors
Developed by: Izzie Nielsen, Becca Borgmeier, and Danielle Carrol
