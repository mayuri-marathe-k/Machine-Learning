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

s = 1236472051807 / 1000.0
t = datetime.datetime.fromtimestamp(s).strftime('%Y-%m-%d %H:%M:%S.%f')

st.write(t)

# pd.to_datetime(df['ds'], format='mixed')
# pd.to_datetime(df['ds'], errors='coerce')
buffer = io.StringIO()
df.info(buf=buffer)
s = buffer.getvalue()
st.text(s)
# pd.to_datetime(df['ds']).dt.strftime('%y-%m-%d')

# df['ds'] = pd.to_datetime(df['ds'], errors='coerce',dayfirst=False, format='%m/%d/%Y')
# df['ds'] = pd.to_datetime(df['ds'], dayfirst=True)

# df.loc[(df['ds'] >= '2023-01-01') & (df['ds'] < '2023-11-30')]
st.write(df)
# m = Prophet()
# m.fit(df)
# future = m.make_future_dataframe(33, freq='D')
# display(future)
# future

# forecast = m.predict(future)
# forecast
# forecast['yhat'].sum()
# fig1 = m.plot(forecast)
# fig2 = m.plot_components(forecast)


# from prophet.plot import plot_plotly, plot_components_plotly
# plot_plotly(m, forecast)


# plot_components_plotly(m, forecast)
