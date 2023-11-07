import streamlit as st
import numpy as np
import pandas as pd
from prophet import Prophet

df = pd.read_csv("sample.csv")
df.dropna(how='any',axis=0)
df[df['Status'].isin(['Approved'])]
df[df['Leave Type'].isin(['Personal Time Off'])]

df['ds'] = pd.to_datetime(df['ds'], errors='coerce',dayfirst=False, format='%Y-%m-%d')

# df['y'] = df['y'].astype(int)
# df['ds'] = pd.to_datetime(df['ds'],format='mixed', dayfirst=True)

# df['ds'] = pd.to_datetime(df.ds)

# df['ds'] = df['ds'].dt.strftime('%Y-%m-%d %H:%M')

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
