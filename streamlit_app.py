import streamlit as st
import pandas as pd 
try:
    from transformers import AutoTokenizer 
except:
    import os
    os.system("pip3 install transformers")

st.title("This is a demo website for the llm checking") 




def main():
    uploaded_file = st.file_uploader(label = 'upload the file')
    if uploaded_file is not None:
        try:
            dataframe = pd.read_csv(uploaded_file)
            st.write(dataframe['text'])
        except:
            pass

if __name__ == '__main__':
    main()
