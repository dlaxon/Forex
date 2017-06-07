__author__ = 'kashif'
## Download historic forex data in candle format for an instrument
## Also keep in pandas data to do further processing as per your needs

from OandaHistoricalData import OandaHistoricalData
import datetime

y = OandaHistoricalData()

granularity = 'H1'
instrument = 'EUR_USD'
start_time = '2017-05-01 00:00'
#end_time = '2018-05-20 22:00'

df = y.getCandlesData(insrtument=instrument, count=4999, candleFormat='midpoint' ,granularity=granularity, start=start_time, end=None, csv='Y', csv_path='/tmp/oanda_files')

print df.head(2)
print type(df)