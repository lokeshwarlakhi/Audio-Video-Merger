import streamlit as st
import pandas as pd
from io import StringIO


add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("compressed folders", "Individual Folders")
)

if add_selectbox == 'compressed folders':
    st.title('Choose the file')
    uploaded_file = st.file_uploader("Browse files")
    if uploaded_file is not None:
        dataframe = pd.read_csv(uploaded_file)
        st.write(dataframe)
