from iexfinance.stocks import Stock, get_historical_data
import matplotlib.pyplot as plt
from datetime import datetime

token = "pk_746a3d87b4a545c09ed8a1336343b981"

def getStockPriceHistoryIEX(ticker, start, end= None):
    if end == None:
        end = datetime.now()
    stockHistory = get_historical_data(ticker,start,end,output_format='pandas', token = token)
    return stockHistory


def plotStockData(stockAsPandas):
    (stockAsPandas.loc[:, stockAsPandas.columns != 'volume']).plot()
    plt.show()

def getStockListPriceHistoryIEX(tickerList, startDate):
    stockDataList = []
    for ticker in tickerList:
        stockDataList.append(getStockPriceHistoryIEX(ticker, startDate))
    return stockDataList