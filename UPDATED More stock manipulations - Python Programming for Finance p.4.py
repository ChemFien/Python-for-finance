import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
style.use('ggplot')

df = pd.read_csv('tsla.csv', parse_dates=True, index_col=0)

##OHLC graph type from matplotlib
from mplfinance  import candlestick_ohlc # requires mdates for each ohlc
import matplotlib.dates as mdates # date type for matplotlib graphs as it does not use datetime dates

# Resample data up or down, up to zoom in
#make a new data frame to resample. Can find D(days) xmin, xmax, xmean, xsum; where x is a given number
df_ohlc = df['Adj Close'].resample('10D').ohlc() # if the company has a stock split you would need to create a data set based on the adjusted close - open high low close

df_volume = df['Volume'].resample('10D').sum() # could use mean for avarage volume

#print(df_ohlc.head())

df_ohlc.reset_index(inplace=True) #resets the index
df_ohlc['Date'] = df_ohlc['Date'].map(mdates.date2num) #converts dates to mdates

ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex=ax1)
ax1.xaxis_date()

candlestick_ohlc(ax1, df_ohlc.values, width=5, colorup='g')
ax2.fill_between(df_volume.index.map(mdates.date2num), df_volume.values, 0)
plt.show()