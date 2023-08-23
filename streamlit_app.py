import streamlit as st
import pandas as pd 
import torch
from transformers import AutoTokenizer 
import requests

st.title("This is a demo website for the llm checking") 



def main():
    BASE_URL = 'http://219.91.172.132:5556'
    input = { "query": 'Give me 2 state names of India'}
    response = requests.post(f"{BASE_URL}/generate", json= input)
    st.write(response.json())


# def main():
#     model_name = 'bert-base-uncased'
#     tokenizer = AutoTokenizer.from_pretrained(model_name) 
#     uploaded_file = st.file_uploader(label = 'upload the file')
#     if uploaded_file is not None:
#         try:
#             dataframe = pd.read_csv(uploaded_file)
#             st.write(tokenizer.tokenize(dataframe['text'][0]))
#         except:
#             pass
        

if __name__ == '__main__':
    main()
