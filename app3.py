import os
import signal
from flask import Flask
from buzz import generator

app = Flask(__name__)

signal.signal(signal.SIGINT, lambda s, f: os._exit(0))

@app.route("/")
def generate_buzz():
    page = '<html><body><h1>'
    page += generator.generate_buzz()
    page += '</h1></body></html>'
    return page

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port=os.getenv('PORT'))

def scrape_stock(stock):
    '''
    This function is designed to scrape the current stock second to second stock prices
    upon at the time the stock is traded (either bought or sold).
    
    This function utilizes beautifulsoup to srape the prices from Yahoo! Finance.
    
    References:
    http://pythoncentral.io/python-beautiful-soup-example-yahoo-finance-scraper/
    https://stackoverflow.com/questions/35439105/scrape-yahoo-finance-income-statement-with-python
    '''
    
    import re, requests
    from urllib.request import urlopen
    from bs4 import BeautifulSoup
    
    url = 'https://finance.yahoo.com/quote/%s?p=%s'%(stock,stock)
    r = requests.get(url)
    
    soup = BeautifulSoup(r.text, 'html.parser')
      
    trade_value = soup.find('span', {'class':'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)'}).getText()
    return(float(trade_value)) 

scrape_stock(AAPL)

#from pandas.io import data, wb # becomes
from pandas_datareader import data, wb
import pandas_datareader as pdr
aapl = pdr.get_data_yahoo('AAPL')
amzn = pdr.get_quote_yahoo('AMZN')
aapl = pdr.get_quote_yahoo('AAPL').last
#print(amzn)
print(aapl)
