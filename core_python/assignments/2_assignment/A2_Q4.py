### WAP to calculate area of triangle and rectangle.

# Take input
tri = input('Enter base and height of triangle (b 000 h 000 cm/m) : ')
rec = input('Enter length and width of rectangle (l 000 w 000 cm/m) : ')

# operation for area triangle
if ('cm' in tri):
    unit = 'cm²'
elif ('m' in tri):
    unit = 'm²' 

t = int(tri.replace('b','').replace(' ','').replace('h','').replace('cm','').replace('m',''))
area_tri = (1/2)*(t//1000)*(t%1000)

print(f'Area of a triangle is {area_tri} {unit}')

# operation for area of rectangle
if ('cm' in rec):
    unit = 'cm²'
elif ('m' in rec):
    unit = 'm²'
    
r = int(rec.replace('l','').replace(' ','').replace('w','').replace('cm','').replace('m',''))
area_rec = (r//1000)*(r%1000)

print(f'Area of rectangle is {area_rec} {unit}')