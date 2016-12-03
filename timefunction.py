from datetime import date

def get_between_days(startdate, enddate):
    d1 = startdate.split('-')
    d2 = enddate.split('-')
    d1 = date(int(d1[0]), int(d1[1]), int(d1[2]))
    d2 = date(int(d2[0]), int(d2[1]), int(d2[2]))
    delta = d2 - d1
    return(delta.days + 1)

#print(get_between_days('2016-11-11', '2016-11-11'))

x = ['2016-11-11', '2016-11-12', '2016-11-13', '2016-11-15', '2016-11-16',
 '2016-11-17', '2016-11-18', '2016-11-19', '2016-11-20', '2016-11-21',
 '2016-11-22', '2016-11-23', '2016-11-24', '2016-11-26', '2016-11-27',
 '2016-11-28', '2016-11-29', '2016-11-30', '2016-12-01', '2016-12-02',
 '2016-12-03']

def get_day_id(list_day):
    new_x = []

    for i in x:
        new_x.append(get_between_days(x[0], i))

    return(new_x)

print(get_day_id(x))