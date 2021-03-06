import datetime


def get_between_days(startdate, enddate):
    d1 = startdate.split('-')
    d2 = enddate.split('-')
    d1 = date(int(d1[0]), int(d1[1]), int(d1[2]))
    d2 = date(int(d2[0]), int(d2[1]), int(d2[2]))
    delta = d2 - d1
    return(delta.days)

def get_range_days(startdate, enddate):
    dlist = []
    dateList = []
    d1 = startdate.split('-')
    d2 = enddate.split('-')
    d1 = datetime.date(int(d1[0]), int(d1[1]), int(d1[2]))
    d2 = datetime.date(int(d2[0]), int(d2[1]), int(d2[2]))
    delta = d2 - d1
    d = delta.days
    for i in range(0, d+1):
        dlist.append(d2 - datetime.timedelta(days=i))

    for i in dlist:
        year = str(i.year)
        if len(str(i.month)) == 2:
            month = str(i.month)
        else:
            month = '0' + str(i.month)
        if len(str(i.day)) == 2:
            day = str(i.day)
        else:
            day = '0' + str(i.day)
        dateList.append("%s-%s-%s" %(year, month, day))

    dateList.reverse()

    return dateList

print(get_range_days('2016-11-11', '2016-12-02'))

#print(get_between_days('2016-11-11', '2016-11-11'))

#x = ['2016-08-15', '2016-08-17', '2016-08-18', '2016-08-19', '2016-08-20', '2016-08-21', '2016-08-23', '2016-08-24', '2016-08-25', '2016-08-27', '2016-08-30', '2016-09-01', '2016-09-02', '2016-09-03', '2016-09-06', '2016-09-10', '2016-09-14', '2016-09-16', '2016-09-17', '2016-09-24', '2016-09-29', '2016-10-02', '2016-10-05', '2016-10-06', '2016-10-07', '2016-10-09', '2016-10-14', '2016-10-15', '2016-10-17', '2016-10-21', '2016-10-22', '2016-10-24', '2016-10-26', '2016-10-29', '2016-11-01', '2016-11-03', '2016-11-04', '2016-11-05', '2016-11-06', '2016-11-08', '2016-11-09', '2016-11-10', '2016-11-11', '2016-11-12', '2016-11-14', '2016-11-15', '2016-11-16', '2016-11-18', '2016-11-19', '2016-11-27', '2016-11-28', '2016-11-30', '2016-12-02']

def get_day_id(list_day):
    new_x = []

    for i in list_day:
        new_x.append(get_between_days(list_day[0], i))

    return(new_x)

#print(get_day_id(x))