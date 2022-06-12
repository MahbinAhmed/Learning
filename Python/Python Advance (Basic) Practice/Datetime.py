from calendar import month
import datetime

''' Datetime module is based on 6 classes
1. date
2. time
3. datetime
4. timedelta
5. tzinfo
6. timezone'''

# Date ======>>>>>

# print(datetime.date(2022,8,10))
# print(datetime.date.today())
# print(datetime.date.today().month)
# print(datetime.date.today().year)
# print(datetime.date.today().day)
# print(datetime.datetime.fromtimestamp(1887639468))
# print(datetime.date.isoformat(datetime.date.today()))

# print(datetime.date.ctime(datetime.date.today()))
# print(datetime.date.isocalendar(2022,5,27))
# print(datetime.date.strftime(datetime.date.today(),"))

# Time =====>>>>>

time = datetime.time(12,39,15)
# print(time)
# print(datetime.time(second=2))
# print(datetime.time())
# print(time.microsecond)
# print(type(datetime.time.isoformat(time)))
# print(datetime.time.dst())
# print(datetime.time.replace(time,11,56,12))
# print(datetime.time.strftime(time))
# print(datetime.time.tzinfo)

# Datetime =====>>>>>

date_time = datetime.datetime(2000,1,12,18,56)
# print(date_time)
# print(date_time.hour)
# print(datetime.datetime.now().second)
# print(datetime.datetime.strftime(date_time))
# print(datetime.datetime.isoformat(date_time))
# print(datetime.datetime.astimezone())
# print(datetime.datetime.time(date_time))
# print(datetime.datetime.strptime("2022-05-27"))
# print(datetime.datetime.today())
# print(datetime.datetime.tzname(date_time))

# Timedelta =====>>>>>
a = datetime.datetime.now() + datetime.timedelta(days=2)
# print(datetime.datetime.now() * datetime.timedelta(days=2.00))
# print(a - datetime.datetime.now())

# Format Datetime =====>>>>>
# strftime()--->>>

current_time = datetime.datetime.now()
# print(current_time.strftime("%A %m %Y"))

# strptime()--->>>
time_format = "25/05/99"
# print(datetime.datetime.strptime(time_format, "%d/%m/%y"))

# Handling time zone =====>>>>>
import pytz
current_time = datetime.datetime.now(pytz.timezone("UTC"))
# print(current_time)
print(current_time.astimezone(pytz.timezone("Asia/Dhaka")))