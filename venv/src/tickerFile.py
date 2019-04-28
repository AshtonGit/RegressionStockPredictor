

# This class performs CRUD operations on a file that stores a list of ticker names
# These files allow convenient grouping and loading of tickers for repeat operations
# over an extented period of time.
import pickle as pk

class TickerFileWriter:
    filename

    def __init__(self, filename):
        self.filename = filename

    #add all tickers in file to list
    def appendTickers(tickers):
        with open(filename, 'wb+rb') as fp:
            tickerList = pk.load(fp)
            for ticker in tickers:
                if ticker not in tickerList:
                    tickerList.append(ticker)
        pk.dump(tickerList,fp)
        close(filename)

    #remove all tickers in tickers from file
    def removeTickers(tickers):
        tickerList = loadListFromFile(filename)
        with open(filename, 'wb+rb') as fp:
            tickerList = pk.load(fp)
            for ticker in tickers
                tickerList.remove(ticker)
        pk.dump(tickerList, fp)
        close(fp)

    #update function. Adds all tickers in list to file and removes all tickers not found in list.
    def updateAllTickers(tickers):
        with open(filename, 'wb+rb') as fp:
            tickerList = pk.load(fp)
            for ticker in tickers:
                if ticker not in tickerList:
                    tickerList.append(ticker)
            for ticker in tickerList:
                if ticker not in tickers:
                    tickerList.remove(ticker)
        pk.dump(tickerList, fp)
        close(fp)


    def setFilename(filename):
        self.filename = filename

    def getFilename():
        return self.filename
