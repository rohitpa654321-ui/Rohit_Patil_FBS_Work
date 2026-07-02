### WAP to input all sides of a triangle and check whether triangle is valid or not.

# Take input
side_a = int(input('Enter 1st side of a triangle : '))
side_b = int(input('Enter 2nd side of a triangle : '))
side_c = int(input('Enter 3rd side of a triangle : '))

# valid if one side is alway greater than the sum of other two sides
_1 = (side_a + side_b) > side_c
_2 = (side_a + side_c) > side_b
_3 = (side_b + side_c) > side_a

# operation with condition
if (_1 == _2 == _3):
    print('Triangle is valid.')
else :
    print('It is not a valid triangle.')

print(_1 ,_2 , _3)