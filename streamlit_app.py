import streamlit as st
import numpy as np
import pandas as pd
import math
from prophet import Prophet

df = pd.read_csv("sample.csv")

df.replace([np.inf, -np.inf], np.nan)
df.dropna(inplace=True)
df.dropna(how='any',axis=0)
df['y'] = df['y'].astype(int)
df['ds'] = pd.to_datetime(df['ds'], format='mixed')

new_df = df[(df['Status'].isin(['Approved'])) & (df['Leave Type'].isin(['Personal Time Off'])) & (df['ds'] >= '2023-01-01') & (df['ds'] < '2023-11-30')]

# buffer = io.StringIO()
# df.info(buf=buffer)
# s = buffer.getvalue()
# st.text(s)


pf = new_df.groupby(['ds'])['y'].sum().reset_index()
st.write(pf)
m = Prophet()
m.fit(pf)
future = m.make_future_dataframe(33, freq='D')



forecast = m.predict(future)
st.write(forecast[['ds','yhat']])

cnt = forecast['yhat'].sum()
st.write('Predicted leaves in 2023 year will be',math.ceil(cnt))
