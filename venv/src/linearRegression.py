import numpy as np
import time
import smtplib
from datetime import datetime


from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_validate
from sklearn import preprocessing, svm


def predictStockPrice(stock, numDays):
    start = datetime(2018, 1, 1)
    end = datetime.now()
    df = get_historical_data(stock, start=start, end = end, output_format='pandas')
    df.to_csv('Predictions/'+stock+'_Prediction.csv')

    df['prediction'] = df['close'].shift(-1)
    df.dropna(inplace=True)
    x = np.array(df.drop(['preditction'], 1))
    y = np.array(['prediction'])
    x = preprocessing.scale(x)
    x_prediction = x[-int(numDays):]
    x_train, x_test, y_train, y_test = cross_validate.train_test_split(x,y,test_size = 0.5)

    clf = LinearRegression()
    clf.fit(c_train, y_train)
    prediction = clf.predict(x_prediction)
    printf(prediction)
    print("hello")
    return prediction


def __init__():

    stockList = getStockData(10)
    for i in stockList:
        try:
            predictStockPrice(i, 3)
        except:
            print("Stock: "+ i + "was not predicted")
