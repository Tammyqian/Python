import datetime
import time

def time_to_timestamp(strtime):
    timeArray = time.strptime(strtime, "%Y-%m-%d %H:%M:%S")
    timeStamp = time.mktime(timeArray)
    return timeStamp

def tss_2_ts(ts):
    dts = (ts[0] + ts[1]) / 2
    return dts

def ts_2_label(dts):
    dateArray = datetime.datetime.utcfromtimestamp(dts)
    day = dateArray.day
    mmonth = dateArray.month
    return '{}/{}'.format(mmonth, day)

def dt():
    month = datetime.datetime.now().month
    year = datetime.datetime.now().year
    day = datetime.datetime.now().day
    if day <=9:
        day = '0{}'.format(day)
    end = time_to_timestamp('{}-{}-{} 00:00:00'.format(year, month, day))
    start = end - 24*3600*7
    tss = []
    for i in range(8):
        tss.append(end-i*24*3600)
    tss.reverse()
    ts_sizes = zip(tss[:-1], tss[1:])