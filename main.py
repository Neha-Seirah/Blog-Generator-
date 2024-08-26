import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
import os
from dotenv import  load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate # Prompt template
# Function to get a response from the LLama 2 model

load_dotenv()

    # LLama 2 model

    # Fill in the prompt template

prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "Act as a blog writer"),
            # If user asked any other unrelated topics, it will not answer. It will respond accordingly.
            ("user", "Question:{question}")
        ]
    )

groqApi = ChatGroq(model="llama3-70b-8192", temperature=0)
outputparser = StrOutputParser()
chainSec = prompt | groqApi | outputparser

# Streamlit App Configuration
st.set_page_config(page_title="Generate Blogs",
                   page_icon='🤖',
                   layout='centered',
                   initial_sidebar_state='collapsed')

st.header("Generate Blogs 🤖")

# User inputs for blog generation
input_text = st.text_input("Enter the Blog Topic")

# Creating two more columns for additional fields
# col1, col2 = st.columns([5, 5])
#
# with col1:
#     no_words = st.text_input('No of Words')
# with col2:
#     blog_style = st.selectbox('Writing the blog for',
#                               ('Researchers', 'Data Scientist', 'Common People'), index=0)

# Generate button
# submit = st.button("Generate")
#
# # Final response display
# if submit:
if input_text:
        st.write(chainSec.invoke({'question':input_text}))
else:
        st.error("Please enter a valid blog topic and number of words.")
