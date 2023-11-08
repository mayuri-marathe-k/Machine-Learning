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
pd.to_datetime(df['ds'], format='mixed')
df[(df['Status'].isin(['Approved'])) & (df['Leave Type'].isin(['Personal Time Off']))]

# leave = df[df['Leave Type'].isin(['Personal Time Off'])]
# st.write(leave)


# df['ds'] = pd.to_datetime(df['ds'], format='mixed')
# st.write(df['ds'])
buffer = io.StringIO()
df.info(buf=buffer)
s = buffer.getvalue()
st.text(s)
