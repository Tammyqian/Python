import time
a = time.time()
date = time.strftime('%Y-%m-%d', time.localtime(a))
print a, date
start = time.mktime(time.strptime(date, '%Y-%m-%d'))
end = time.time()
print time.strftime('%Y-%m-%d %H%M%S')
print start
print end