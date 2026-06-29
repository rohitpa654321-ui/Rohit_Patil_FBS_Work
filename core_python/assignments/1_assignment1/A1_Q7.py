import math
### Program to find the roots ofa quadratic equation.

# Take input
a = int(input('Enter a :'))
b = int(input('Enter b :'))
c = int(input('Enter c :'))

# Perform Operation
d = b**2 -4*a*c

if (d>0):
    root1 = (-b+ (b**0.5)-(2*a*c))/2*a
    root2 = (-b- (b**0.5)-(2*a*c))/2*a
    print(f'Roots are {root1} and {root2}')
elif (d==0):
    root1 = root2 = (-b+ (b**0.5)-(2*a*c))/2*a
    print(f'Roots are {root1} and {root2}')

else:
    print('Root does not exist...')
    
