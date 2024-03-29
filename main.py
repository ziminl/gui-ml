# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ItV1Nb-n0OXdpIOtRsAuWQ5s1ELTpqb8
"""

import pandas as pd
import yfinance as yf


dfSPY=yf.download("^RUI",start='2011-01-05', end='2021-01-05')

dfSPY=dfSPY[dfSPY.High!=dfSPY.Low]
dfSPY.reset_index(inplace=True)
dfSPY.head()

pip install Backtesting pandas_ta

import pandas_ta as ta
dfSPY['EMA']=ta.sma(dfSPY.Close, length=200)
dfSPY['RSI']=ta.rsi(dfSPY.Close, length=2)
my_bbands = ta.bbands(dfSPY.Close, length=20, std=2.5)
my_bbands[0:50]
dfSPY=dfSPY.join(my_bbands)
dfSPY.dropna(inplace=True)
dfSPY.reset_index(inplace=True)
dfSPY

def addemasignal(df, backcandles):
    emasignal = [0]*len(df)
    for row in range(backcandles, len(df)):
        upt = 1
        dnt = 1
        for i in range(row-backcandles, row+1):
            if df.High[i]>=df.EMA[i]:
                dnt=0
            if df.Low[i]<=df.EMA[i]:
                upt=0
        if upt==1 and dnt==1:
            emasignal[row]=3
        elif upt==1:
            emasignal[row]=2
        elif dnt==1:
            emasignal[row]=1
    df['EMASignal'] = emasignal

addemasignal(dfSPY, 6)

def addorderslimit(df, percent):
    ordersignal=[0]*len(df)
    for i in range(1, len(df)): 
        if df.EMASignal[i]==2 and df.Close[i]<=df['BBL_20_2.5'][i]:
            ordersignal[i]=df.Close[i]-df.Close[i]*percent
        elif df.EMASignal[i]==1 and df.Close[i]>=df['BBU_20_2.5'][i]:
            ordersignal[i]=df.Close[i]+df.Close[i]*percent
    df['ordersignal']=ordersignal

addorderslimit(dfSPY, 0.00)

dfSPY[dfSPY.ordersignal!=0]

import numpy as np
def pointposbreak(x):
    if x['ordersignal']!=0:
        return x['ordersignal']
    else:
        return np.nan
dfSPY['pointposbreak'] = dfSPY.apply(lambda row: pointposbreak(row), axis=1)

import plotly.graph_objects as go
from plotly.subplots import make_subplots
from datetime import datetime

dfpl = dfSPY[1000:1250].copy()
fig = go.Figure(data=[go.Candlestick(x=dfpl.index,
                open=dfpl['Open'],
                high=dfpl['High'],
                low=dfpl['Low'],
                close=dfpl['Close']),
                go.Scatter(x=dfpl.index, y=dfpl.EMA, line=dict(color='orange', width=2), name="EMA"),
                go.Scatter(x=dfpl.index, y=dfpl['BBL_20_2.5'], line=dict(color='blue', width=1), name="BBL_20_2.5"),
                go.Scatter(x=dfpl.index, y=dfpl['BBU_20_2.5'], line=dict(color='blue', width=1), name="BBU_20_2.5")])

fig.add_scatter(x=dfpl.index, y=dfpl['pointposbreak'], mode="markers",
                marker=dict(size=5, color="MediumPurple"),
                name="Signal")
fig.show()
