
### datetime module

from datetime import datetime , date , timedelta


# %d             Day

# %m             Month

# %Y             Four-digit year

# %H             Hour (24-hour)

# %M             Minute

# %S             Second

# %A             Full weekday name

# %B             Full month name




# datetime.now() 
n = datetime.now()

print(n)
print(n.year)
print(n.month)
print(n.day)
print(n.hour)
print(n.minute)
print(n.second)


print(datetime.today())

print(datetime(2026, 10, 7))

dt = datetime(2026, 10, 7)
print(dt.strftime("%d-%m-%Y"))                               # datetime to string

dt = datetime.strptime("07-10-2026", "%d-%m-%Y")             # string to datetime
print(dt)

print(date.today())

print(dt.weekday())  # 0 = Monday, 6 = Sunday

print(dt.replace(year=2027))   

dt = datetime(2026, 10, 7)
print(dt + timedelta(days=5))
print(dt - timedelta(days=5))



import time

print(time.time())  # seconds since epoch  in miniseconds

# sleep
for i in range(5):
    print(i)
    time.sleep(1)  # sleep for 1 second
    

print(time.localtime())  # current time in string format