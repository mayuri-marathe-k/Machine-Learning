import streamlit as st
# pip install pystan
# pip install prophet
# from prophet import Prophet
# import numpy as np
import pandas as pd

df = pd.read_csv("sample.csv")
df.dropna(how='any',axis=0)
df[df['Status'].isin(['Approved'])]
df[df['Leave Type'].isin(['Personal Time Off'])]
# df['y'] = df['y'].astype(int)
# df['ds'] = pd.to_datetime(df['ds'])
df.loc[(df['ds'] >= '2023-01-01') & (df['ds'] < '2023-11-30')]
st.write(df.head())
