from yahoo_finance import Share



def get_historical_price(startdate, enddate):
    nya = Share('NYA')
    date_adj_close = []
    historical_data = nya.get_historical(startdate, enddate)

    for i in historical_data:
        date_adj_close.append([i['Date'], i['Adj_Close']])

    return date_adj_close[::-1]


print(get_historical_price('2016-11-11', '2016-12-03'))
