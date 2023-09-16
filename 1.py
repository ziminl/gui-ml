import pandas as pd
import yfinance as yf


dfSPY=yf.download("^RUI",start='2011-01-05', end='2021-01-05')
#dfSPY=yf.download("EURUSD=X",start='2011-01-05', end='2021-01-05')

dfSPY=dfSPY[dfSPY.High!=dfSPY.Low]
dfSPY.reset_index(inplace=True)
dfSPY.head()
