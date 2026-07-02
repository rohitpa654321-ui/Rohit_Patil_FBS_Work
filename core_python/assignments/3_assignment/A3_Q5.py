### WAP to check whether the triangle is equilateral, isosceles or scalene

# Take input



a = int(input('Enter 1st side of a triangle : '))
b = int(input('Enter 2nd side of a triangle : '))
c = int(input('Enter 3rd side of a triangle : '))

# operation with conditon
if ((a+b>c)==(a+c>b)==(b+c>a)):
    if ((a == b == c)):
        print('Triangle is an equilateral triangle : Its all sides and angles are equal.')
    elif ((a==b)or(b==c)or(c==a)):
        print('It is an isosceles triangle : Two sides are equal and opposite angles are equal of same sides.')
    # elif ((a==b)and(b!=c)and(c!=a)):
    #     print('It is a scelene triangle : Its all sides and angles are different.')
    else:
        print('It is a scelene triangle : Its all sides and angles are different.')
        