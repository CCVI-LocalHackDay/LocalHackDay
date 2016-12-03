from yahoo_finance import Share

nasdaq = Share('^IXIC')


def get_historical_price(startdate, enddate):
    date_adj_close = []
    historical_data = nasdaq.get_historical(startdate, enddate)

    for i in historical_data:
        date_adj_close.append([i['Date'], i['Adj_Close']])

    return date_adj_close[::-1]


print(get_historical_price('2016-11-30', '2016-12-02'))
