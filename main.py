from dotenv import load_dotenv
import os
import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from langchain.callbacks import get_openai_callback

def main():
    try:
        load_dotenv()
        st.title("PDF Prompter")
        st.header("Ask your PDF a question...any question")
    
        # Upload the pdf
        pdf=st.file_uploader ("Upload your PDF", type="pdf")
    
        # Extract the text
        if pdf is not None:
            pdf_reader = PdfReader(pdf)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()
            
            # Split into chuncks
            text_splitter = CharacterTextSplitter(
                separator="\n", 
                chunk_size=1000,
                chunk_overlap=200,
                length_function=len)
            chunks=text_splitter.split_text(text)
        
            # Create PDF chunk embeddings
            embeddings = OpenAIEmbeddings()
            knowldege_base = FAISS.from_texts(chunks, embeddings)
       
            # Show user imput
            user_prompt = st.text_input("Write a prompt-question about your PDF")
            if user_prompt:
                docs = knowldege_base.similarity_search(user_prompt)
             
                llm = OpenAI()          
                chain = load_qa_chain(llm, chain_type="stuff")
                #with get_openai_callback as cb:
                response = chain.run(input_documents=docs, question=user_prompt)
                   # print(cb)
            
                st.write(response)
                
    except Exception as e:
        st.write("An error occurred: ", str(e))
        

if __name__ == "__main__":
    main()
