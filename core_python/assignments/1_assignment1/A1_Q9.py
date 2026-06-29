### Write a program to enter base and height of a triangle and find its area.

# Take input
b = int(input('Enter base of triangle in cm :'))
h = int(input('Enter height of triangle in cm :'))

# perform operation
area_rec = 1/2*b*h

# Display result
print(f'Area of triangle is :{area_rec} cmsq.')