import calendar
from datetime import datetime
import time
import pytz
'''
print(time.time())
print(time.asctime())
varshi=datetime.datetime.now()

print("year", varshi.year)


s=calendar.prcal(2004)
s2=calendar.month(2004,3)
s1=calendar.isleap(2005)
print(s1)

x=datetime.datetime.now()
from datetime import timedelta
print(x+timedelta(days=-89))
'''
time1 = pytz.timezone('UTC')
print("Current Time is: ",datetime.now(time1))