### Write a program to accept distance in km and convert it into meter and centimeters both.

# Take input
dist = float(input('Enter distance in km : '))

# perform operation
mtr = dist * 1000
cm = mtr * 100

# Display 
print(f'Given distance in km can be in meter {mtr}m and in centimeter {cm}cm ')
