### Write a program to find the area and perimeter of following figure.
# (Accept the length , breadth and radus from user:)

#  ------------.
# !              .)
# !              .)
#  ------------.


# Input
l = int(input('Enter length in cm :'))
b = int(input('Enter breadth in cm :'))
r = int(input('Enter radius in cm :'))

# Operation 

rec_per = 2*(l+b)
rec_area = l*b

hc_per = (1/2)*(2*3.14*r)
hc_area =(1/2)*(3.14*r*r)

# final operation

perimeter = rec_per + hc_per
area = rec_area + hc_area

# Display result

print(f'Perimeter of given figure is :{perimeter} cm.')
print(f'Area of given figure is : {area}cmsq.')