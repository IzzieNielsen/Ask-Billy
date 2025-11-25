import streamlit as st
import text_processor as backend

#page setup
st.set_page_config(page_title = "ASK BILLY", layout = "wide")
st.title("Ask Billy")
st.write("Ask me questions about Creighton University!")

#image
st.image("creightonlogo.png", width = 200)

#chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

#chat display
for sender, msg in st.session_state.messages:
    st.chat_message(sender).write(msg)

#get user input
user_input = st.chat_input("Ask a question")

if user_input:
    st.session_state.messages.append(("user", user_input))
    st.chat_message ("user").write(user_input)

    with st.spinner("thinking"):
        result = backend.qa_chain({"query": user_input})
        answer = result ["result"]
        src = result["source_documents"]

    st.session_state.messages.append(("billy", answer))
    st.chat_message("billy").write(answer)


