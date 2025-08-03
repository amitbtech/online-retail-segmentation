import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import streamlit as st
import pandas as pd
from src.segmentation import perform_rfm_segmentation
from src.visualizer import save_cluster_boxplots

st.title("Customer Segmentation: Online Retail")

uploaded_file = st.file_uploader("Upload OnlineRetail CSV", type="csv")
if uploaded_file:
    df = pd.read_csv(uploaded_file, encoding='ISO-8859-1')
    st.write("Sample Data", df.head())
    rfm = perform_rfm_segmentation(df)
    save_cluster_boxplots(rfm)
    st.write("RFM Segmentation Result", rfm.groupby('Cluster').mean())
    st.image("visuals/rfm_cluster_boxplots.png", caption="Cluster Boxplots", use_column_width=True)
