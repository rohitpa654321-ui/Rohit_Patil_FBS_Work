### convert distance given in feet and inch to meter and centimeter.

# Take input 
dist = input('Enter distance in feet and inch (12f 21i) : ')
n = int(dist.replace('f','').replace(' ','').replace('i',''))
feet = n//100
inch = n%100

# perform operation
print(f'The distance in meter and centimeter is : {feet*0.3048} m {inch*2.54} inch .')