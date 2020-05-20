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
    print('Welcome to my regression stock price predictor')
    print('First enter the 3 letter id for the stock you want predicted \n\t eg "NKE')
    print('Then enter the date from which stock analysis will start from \n\t eg 01 05 2018')
    print('Lastly enter how many days into the future you want the prediction to extend \n\t eg 5')
    today = datetime.date.today()
    while True:
        ticker = input('\n\nStock ticker:').strip().upper()
        if len(ticker) != 3:
            print('Sorry, stock ticker must be exactly 3 characters long')
            continue

        s = input("Start date (dd mm yyyy):").split()
        try:
            start = datetime.date(int(s[2]), int(s[1]), int(s[0]))
        except ValueError:
            print('Sorry, invalid date given')
            continue

        days_in = input("Prediction length (days): ")
        try:
            numDays = int(days_in)
        except ValueError:
            print("Input must be a whole number")
            continue

        prediction = predictStockLinearRegression(ticker,numDays, start, today)
        print('Predicted',ticker,'stock price over the coming',str(numDays),'days:')
        print(prediction)


main()