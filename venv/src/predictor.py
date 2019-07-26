import numpy as np
import time
import smtplib
import datetime
from dataParser import getStockPriceHistoryIEX, plotStockData


from sklearn.linear_model import LinearRegression
from sklearn.svm import LinearSVR
from sklearn.model_selection import train_test_split
from sklearn import preprocessing, svm, metrics

def predictStockSVR(stock, numDays, start = None, end = None):
    if start == None:
        start = datetime.date(2018,1,1)
    if end == None:
        end = datetime.now()

    df = getStockPriceHistoryIEX(stock, start, end)
    label = df['close'].shift(-numDays)
    X = np.array(df[['close']])
    X = preprocessing.scale(X)
    X_lately = X[-numDays:]
    X = X[:-numDays]
    label.dropna(inplace=True)
    Y = np.array(label)
    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.3)
    svr = LinearRegression()
    svr.fit(x_train, y_train)
    score = svr.score(x_test,y_test)
    print("Score: "+str(score))
    prediction = svr.predict(X_lately)
    return prediction


def predictStockLinearRegression(stock, numDays, start = None, end = None):
    if start == None:
        start = datetime.date(2018,1,1)
    if end == None:
        end = datetime.now()

    df = getStockPriceHistoryIEX(stock, start, end)
    label = df['close'].shift(-numDays)
    X = np.array(df[['close']])
    X = preprocessing.scale(X)
    X_lately = X[-numDays:]
    X = X[:-numDays]
    label.dropna(inplace=True)
    Y = np.array(label)
    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.3)
    clf = LinearRegression()
    clf.fit(x_train, y_train)
    score = clf.score(x_test,y_test)
    print("Score: "+str(score))
    prediction = clf.predict(X_lately)
    return prediction

def getAccuracy(prediction, y_true, predictedCol,numDays):
    y_true = np.array(y_true[predictedCol].tail(numDays))
    print("Predicted Values:")
    print(prediction)
    print("Real Values:")
    print(y_true)
    acc = metrics.regression.mean_squared_error(y_true, prediction)
    print("accuracy: "+str(acc))

def main():
    stockData = getStockPriceHistoryIEX("NKE", datetime.date(2018,1,1), datetime.date(2019, 1, 30))
    prediction = predictStockLinearRegression("NKE",5,start = datetime.date(2018,1,1),
                                   end = datetime.date(2019,1,20))
    print("Linear Regression: ")
    getAccuracy(prediction, stockData, 'close', 5)

main()