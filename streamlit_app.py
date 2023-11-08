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
df['ds'] = pd.to_datetime(df['ds'], format='mixed')
df[(df['Status'].isin(['Approved'])) & (df['Leave Type'].isin(['Personal Time Off']))]

# buffer = io.StringIO()
# df.info(buf=buffer)
# s = buffer.getvalue()
# st.text(s)

df.loc[(df['ds'] >= '2023-01-01') & (df['ds'] < '2023-11-30')]

m = Prophet()
m.fit(df)
future = m.make_future_dataframe(33, freq='D')
st.write(future)
