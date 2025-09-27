import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="📘 Interactive Textbook Assistant", layout="wide")
st.title("📘 Interactive Textbook Assistant")

uploaded_file = st.file_uploader("Upload a textbook (PDF)", type="pdf")
if uploaded_file:
    files = {"file": uploaded_file.getvalue()}
    response = requests.post(f"{API_URL}/upload_pdf", files={"file": uploaded_file})
    if response.status_code == 200:
        st.success("✅ PDF uploaded & indexed successfully!")


if "history" not in st.session_state:
    st.session_state.history = []

question = st.text_input("Ask a question about the textbook:")

if st.button("Ask") and question:
    response = requests.post(f"{API_URL}/ask", data={"question": question})
    answer = response.json().get("answer", "No answer returned.")
    

    st.session_state.history.append({"question": question, "answer": answer})
    

for chat in reversed(st.session_state.history):
    st.markdown(f"**You:** {chat['question']}")
    st.markdown(f"**Bot:** {chat['answer']}")
    st.markdown("---")

