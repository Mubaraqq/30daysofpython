
import datetime
print(dir(datetime))

# getting datetime information
from datetime import datetime
now = datetime.now()
print(datetime.now())
print(now)
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
second = now.second
timestamp = now.timestamp()
print(day, month, year, hour, minute)
print('timestamp', timestamp)
print(f'{day}/{month}/{year}, {hour}:{minute}')

# formattind date output using strftime
from datetime import datetime
new_year = datetime(2020, 1, 1)
#print(new_year)
day = new_year.day
month = new_year.month
year = new_year.year
hour = new_year.hour
minute = new_year.minute
second = new_year.second
print(day, month, year, hour, minute)
print(f'{day}/{month}/{year}, {hour}:{minute}')

from datetime import datetime
# current date and time
now = datetime.now()
t = now.strftime('%H:%M:%S')
print('time:', t)
time_one = now.strftime('%m/%d/%y, %H:%M:%S')
print('time one:', time_one)
time_two = now.strftime('%d/%m/%y, %H:%M:%S')
print('time two:', time_two)

# string to time using 'strptime'
from datetime import datetime
date_string = '5 December, 2020'
print('date_string = ', date_string)
date_object = datetime.strptime(date_string, "%d %B, %Y")
print('date_object = ', date_object)

# using date from datetime
from datetime import date
d = date(2022, 1, 1)
print(d)
print('current date:', d.today())
# date object of today's date
today = date.today()
print('current year:', today.year)
print('current month:', today.month)
print('current day:', today.day)

# time object to represent time
from datetime import time
a = time() # hour = 0, minute = 0, second = 0
print('a =', a)
b = time(10, 30, 50) # hour = 10, minute = 30, second = 50
print('b =', b)
c = time(hour = 5, minute = 38, second = 45)
print('c =', c)
d = time(7, 30, 50, 200543) # h, m, s, microsecond
print('d =', d)

# difference between two points in time using
from datetime import date, datetime
today = date(year = 2025, month = 7, day = 31)
new_year = date(year = 2026, month = 1, day = 1)
time_left_for_new_year = new_year - today
print('time left for new year =', time_left_for_new_year)

t1 = datetime(year = 2025, month = 5, day = 30, hour = 16, minute = 8, second = 0)
t2 = datetime(year = 2026, month = 1, day = 1, hour = 0, minute = 0, second = 0)
diff = t2 - t1
print('time left for new year =', diff)

############################ EXERCISES ############################################