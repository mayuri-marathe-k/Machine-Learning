import streamlit as st
# pip install pystan
# pip install prophet
# from prophet import Prophet
# import numpy as np
import pandas as pd

df = pd.read_csv("sample.csv")
st.write(df.head())
