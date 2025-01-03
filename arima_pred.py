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

Start='2015-01-01'
Today = date.today().strftime("%Y-%m-%d")
stocks=st.text_input('Enter Stock Ticker','SBIN.NS')
data=yf.Ticker(stocks)


def load():
    data=yf.Ticker(stocks)
    hys_data=data.history(period='10y')
    hys_data.reset_index(inplace=True)
    return hys_data.tail()
st.write(load())    
hys_data=data.history(period='10y')
hys_data.reset_index(inplace=True)

def open():
    df1=hys_data.reset_index()['Open']
    model=ARIMA(df1,order=(2,1,3))
    result=model.fit()
    forecast_steps=5
    forecast_values=result.predict(start=len(df1),end=len(df1)+forecast_steps-1,dynamic=False)
    return forecast_values
    
def high():
    df1=hys_data.reset_index()['High']
    model=ARIMA(df1,order=(2,1,3))
    result=model.fit()
    forecast_steps=5
    forecast_values=result.predict(start=len(df1),end=len(df1)+forecast_steps-1,dynamic=False)
    return forecast_values
   
def low():
    df1=hys_data.reset_index()['Low']
    model=ARIMA(df1,order=(2,1,3))
    result=model.fit()
    forecast_steps=5
    forecast_values=result.predict(start=len(df1),end=len(df1)+forecast_steps-1,dynamic=False)
    return forecast_values 
    
def close():
    df1=hys_data.reset_index()['Close']
    model=ARIMA(df1,order=(2,1,3))
    result=model.fit()
    forecast_steps=5
    forecast_values=result.predict(start=len(df1),end=len(df1)+forecast_steps-1,dynamic=False)
    return forecast_values  
    
st.subheader(':orange[Prediction] :red[of the] :green[Stock Selected]')     
  
opt=['OPEN','HIGH','LOW','CLOSE']
selection=st.selectbox(":rainbow[Select your Prediction for]",options=opt)

if selection=='OPEN':
    st.write(open())
if selection=='HIGH':
    st.write(high()) 
if selection=='LOW':
    st.write(low())  
if selection=='CLOSE':
    st.write(close())         




                   
    
    



 
