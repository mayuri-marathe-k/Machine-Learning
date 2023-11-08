import streamlit as st
import numpy as np
import pandas as pd
import io
import datetime
from prophet import Prophet

df = pd.read_csv("sample.csv")
df.replace([np.inf, -np.inf], np.nan)
df.dropna(inplace=True)
df.dropna(how='any',axis=0)
df['y'] = df['y'].astype(int)
df[df['Status'].isin(['Approved'])]
df[df['Leave Type'].isin(['Personal Time Off'])]



df['ds'] = pd.to_datetime(df['ds'], errors='coerce', format='%Y-%m-%d')
buffer = io.StringIO()
df.info(buf=buffer)
s = buffer.getvalue()
st.text(s)
