import streamlit as st
import pandas as pd
st.title("Bioinformatics Tools List")
adr = st.text("Bioinformatics has a lots of tools in various topics. "
              "In this EXCEL sheet there are some tools links which are used in BI. "
              "Download the EXCEL sheet, search the selected topic, or expand for free ")

dataset = pd.read_csv('1.csv')
st.dataframe(dataset)
