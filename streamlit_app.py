import streamlit as st
import pandas as pd 
# from transformers import AutoTokenizer 

st.title("This is a demo website for the llm checking") 




uploaded_file = st.file_uploader("Choose a file")

dataframe = pd.read_csv(uploaded_file)
    
st.write(dataframe['text'])

# name =  st.text_input('enter your name')

# st.write(f'the name you have entered is {name}')
