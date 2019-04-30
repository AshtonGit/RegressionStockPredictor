

# This class performs CRUD operations on a file that stores a list of ticker names
# These files allow convenient grouping and loading of tickers for repeat operations
# over an extented period of time.
import pickle as pk

class TickerFileWriter:


    def __init__(self, filename):
        self.filename = filename

    #add all tickers in file to list
    def appendTickers(self,tickers):
        tickerList = self.readListFromFile()
        for ticker in tickers:
            if ticker not in tickerList:
                tickerList.append(ticker)

        fp = open(self.filename, "wb")
        pk.dump(tickerList,fp)
        fp.close()

    #remove all tickers in tickers from file
    def removeTickers(self,tickers):
        tickerList = self.readListFromFile()
        for ticker in tickers:
            tickerList.remove(ticker)
        fp = open(self.filename, "wb")
        pk.dump(tickerList, fp)
        fp.close()

    #update function. Adds all tickers in list to file and removes all tickers not found in list.
    def updateAllTickers(self,tickers):
        tickerList = self.readListFromFile()
        removeList = []
        for ticker in tickers:
            if ticker not in tickerList:
                tickerList.append(ticker)
        for ticker in tickerList:
            if ticker not in tickers:
                removeList.append(ticker)
        for ticker in removeList:
            tickerList.remove(ticker)
        fp = open(self.filename, "wb")
        pk.dump(tickerList, fp)
        fp.close()

    def readListFromFile(self):
        try:
            fp = open(self.filename, "rb+")
            tickerList = pk.load(fp)
            fp.close()
        except EOFError:
            tickerList = []
        return tickerList

    def printTickerFile(self):
        try:
            with open(self.filename, 'rb') as fp:
                print(pk.load(fp))
        except EOFError:
            print("File Empty")

    def setFilename(filename):
        self.filename = filename

    def getFilename():
        return self.filename

tickerL = ["ASX", "NKE", "NVD", "LMO"]
tk = TickerFileWriter("../predictions/top_performers")
tk.appendTickers(tickerL)
tk.printTickerFile()
tk.removeTickers(["ASX", "BDE"])
tk.printTickerFile()