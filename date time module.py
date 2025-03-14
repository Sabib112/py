import time, datetime

today=datetime.datetime.now()
print(today)
print(today.year)
print(today.strftime("%A"))
print(today.month)
print(today.day)

newdate=datetime.datetime(2020, 5, 17)
print(newdate)