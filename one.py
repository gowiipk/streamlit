import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# STOCK APP

closing price and volume of google!

""")
#define ticker symbol
tickerSymbol='GOOGL'
#get data on this ticker
tickerData=yf.Ticker(tickerSymbol)
#get historical prices for this ticker
tickerDf=tickerData.history(period='id',start='2010-5-31',end='2020-5-31')
st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)