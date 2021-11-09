#wget the get-pip.py file
wget https://bootstrap.pypa.io/pip/2.7/get-pip.py
#Run the file with python2 get-pip.py
python get-pip
#Install xlrd==1.1.0
python -m pip2 install --user xlrd==1.1.0
import streamlit as st

import pandas as pd

# configuration
st.set_option('deprecation.showfileUploaderEncoding', False)

# title of the app
st.title("Data Visualization App")

# Add a sidebar
st.sidebar.subheader("Visualization Settings")

# Setup file upload
uploaded_file = st.sidebar.file_uploader(
                        label="Upload your CSV or Excel file. (200MB max)",
                         type=['csv', 'xlsx'])

global df
if uploaded_file is not None:
    print(uploaded_file)
    print("hello")

    try:
        df = pd.read_csv(uploaded_file)
    except Exception as e:
        print(e)
        df = pd.read_excel(uploaded_file)

global numeric_columns
global non_numeric_columns
st.write("Please upload file to the application.")

