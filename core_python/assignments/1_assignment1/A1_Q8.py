### Write a program to convert days into year,month,week and day

# Input
days = 500

# perform operation
# year
year = days // 365
days = days % 365

# month
month = days//30
days = days%30

# week
week = days//7

# days
days = days%7

# Display result
print(f'Days converted in ymwd as year: {year} , months : {month}, week :{week}, day :{days}')