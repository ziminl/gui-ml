import pandas_ta as ta
dfSPY['EMA']=ta.sma(dfSPY.Close, length=200)#sma ema
dfSPY['RSI']=ta.rsi(dfSPY.Close, length=2)

my_bbands = ta.bbands(dfSPY.Close, length=20, std=2.5)
my_bbands[0:50]
dfSPY=dfSPY.join(my_bbands)
dfSPY.dropna(inplace=True)
dfSPY.reset_index(inplace=True)
dfSPY
