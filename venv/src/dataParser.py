
from selenium import webdriver
from datetime import datetime


def getStockData(numStocks):
    driver = webdriver.Chrome('C:/Users/Ashton/Downloads/chromedriver_win32')
    url = "https://finance.yahoo.com/screener/predefined/most_actives?offset=0&count=200"
    driver.get(url)
    stockList = []

    for i in range(1, numStocks+1):
        stockTicker = driver.find_element_by_xpath(
            '//*[@id="scr-res-table"]/div[1]/table/tbody/tr['+str(i)+']/td[1]/a'
        )
        stocklist.append(stockTicker.text)
    driver.quit()
    return stockList
