import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from streamlit_extras.add_vertical_space import add_vertical_space

# create a simple GUI

with st.sidebar:

    st.title("ZimaMoto Helps You Make NONDO for your Exams ")

    st.markdown('''
    ## About
    
    This is ChatGPT meets your Professors' Lecture Notes
    
    > [chatGPT](https://chat.openai.com/)
    
    > [Streamlit](https://streamlit.io/)
    '''
    )
    add_vertical_space(40)
    st.write("You Will ❤️ It")

    def main():
        st.write("Hello")
def main():
    st.header(" Chat with ZimaMoto")

    # Upload a pdf file

    pdf = st.file_uploader('Upload your PDF', type='pdf')
    st.write(pdf)
    if pdf is not None:
        pdf_reader = PdfReader(pdf)

        text = ""

        for page in pdf_reader.pages:
            text+=page.extract_text()

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len
        )

        chunks=text_splitter.split_text(text=text)
        st.write(chunks)


if __name__=='__main__':
    main()
