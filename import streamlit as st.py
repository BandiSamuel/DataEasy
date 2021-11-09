
import streamlit as st
import numpy as np
from PIL import Image
import cv2

file = st.file_uploader("Choose an excel file", type="xlsx")

if st.button('go!'):
        
    all_sheet = pd.ExcelFile(file)   
    sheets = all_sheet.sheet_names

    for i in range(len(sheets)):
        df = pd.read_excel(file, sheet_name = sheets[i])
