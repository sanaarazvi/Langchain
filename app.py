import streamlit as st
import PyPDF2


st.title("Interactive PDF Q&A")


uploaded_file = st.file_uploader("Upload your PDF", type="pdf")

if uploaded_file is not None:
 
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()

    st.write("PDF loaded successfully!")


    question = st.text_input("Ask a question about this PDF:")

    if question:
       
        if question.lower() in text.lower():
            st.write("Answer found in the PDF!")
        else:
            st.write("No exact match found. Try rephrasing your question.")

