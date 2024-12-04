import streamlit as st 
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import pandas_datareader as data 
import yfinance as yf
from datetime import date
from statsmodels.tsa.arima.model import ARIMA
import statsmodels.api as sm

st.header('Stock :orange[Web] :red[App]')
st.image("https://th.bing.com/th/id/OIP.Ttoy04OYis0BLYxlPZvTSwHaEK?w=331&h=186&c=7&r=0&o=5&dpr=1.3&pid=1.7")
st.subheader(':rainbow[Stock Future Prediction]')
stocks=st.text_input('Enter Stock Ticker','SBIN.NS')
Start='2015-01-01'
Today = date.today().strftime("%Y-%m-%d")

button1=st.button("Load Data")

if button1:
    data=yf.Ticker(stocks)
    hys_data=data.history(period='10y')
    hys_data.reset_index(inplace=True)
    st.write(hys_data.tail())
    
st.subheader(':orange[Prrediction] :red[of the] :green[Stock Selected]') 
data=yf.Ticker(stocks)
hys_data=data.history(period='10y')  

opt = st.radio(':rainbow[Market Status :]',['Open','High','Low','Close'],horizontal=True) 

if opt=='Open':
    df1=hys_data.reset_index()['Open']
    model=ARIMA(df1,order=(2,1,3))
    result=model.fit()
    forecast_steps=5
    forecast_values=result.predict(start=len(df1),end=len(df1)+forecast_steps-1,dynamic=False)
    st.write(forecast_values)
    
elif opt=='High':
    df1=hys_data.reset_index()['High']
    model=ARIMA(df1,order=(2,1,3))
    result=model.fit()
    forecast_steps=5
    forecast_values=result.predict(start=len(df1),end=len(df1)+forecast_steps-1,dynamic=False)
    st.write(forecast_values) 
    
elif opt=='Low':
    df1=hys_data.reset_index()['Low']
    model=ARIMA(df1,order=(2,1,3))
    result=model.fit()
    forecast_steps=5
    forecast_values=result.predict(start=len(df1),end=len(df1)+forecast_steps-1,dynamic=False)
    st.write(forecast_values) 
    
elif opt=='Close':
    df1=hys_data.reset_index()['Close']
    model=ARIMA(df1,order=(2,1,3))
    result=model.fit()
    forecast_steps=5
    forecast_values=result.predict(start=len(df1),end=len(df1)+forecast_steps-1,dynamic=False)
    st.write(forecast_values)     
