from iexfinance.stocks import Stock, get_historical_data
import matplotlib.pyplot as plt
from datetime import datetime



def getStockPriceHistoryIEX(ticker, startDate):
    endDate = datetime.now()
    stockHistory = get_historical_data(ticker,startDate,endDate,output_format='pandas')
    return stockHistory


def plotStockData(stockAsPandas):
    (stockAsPandas.loc[:, stockAsPandas.columns != 'volume']).plot()
    plt.show()

def getStockListPriceHistoryIEX(tickerList, startDate):
    stockDataList = []
    for ticker in tickerList:
        stockDataList.append(getStockPriceHistoryIEX(ticker, startDate))
    return stockDataList