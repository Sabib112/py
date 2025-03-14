import random 
import time

def get_random_date(startdate,enddate):
    print(f"printing random date between")
    random_generator = random.random()
    date_format = "%m/%d/%Y"

    startdate= time.mktime(time.strptime(startdate, date_format))
    enddate= time.mktime(time.strptime(enddate, date_format))

    random_time = startdate + random_generator * (enddate - startdate)
    random_date= time.strftime(date_format, time.localtime(random_time))
    return random_date

print(get_random_date("1/1/2000", "1/1/2020"))