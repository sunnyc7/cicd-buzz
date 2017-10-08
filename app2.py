import pandas_datareader.data as web
import datetime as dt     
date = dt.date.today
print(date)
#print(datetime.datetime(2010, 1, 1))


# end = datetime.datetime(2013, 1, 27)
# f = web.DataReader("F", 'yahoo', start, end)
# f.ix['2010-01-04']

from pandas.io import data, wb # becomes
from pandas_datareader import data, wb
import pandas_datareader as pdr
pdr.get_data_yahoo('AAPL')
