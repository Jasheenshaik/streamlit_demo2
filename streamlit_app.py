import streamlit as st
import pandas as pd 
import torch
from transformers import AutoTokenizer 

st.title("This is a demo website for the llm checking") 




def main():
    # model_name = 'bert-base-uncased'
    # tokenizer = AutoTokenizer.from_pretrained(model_name) 
    uploaded_file = st.file_uploader(label = 'upload the file')
    if uploaded_file is not None:
        try:
            dataframe = pd.read_csv(uploaded_file)
            st.write(dataframe['text'][0])
        except:
            pass
        

if __name__ == '__main__':
    main()
