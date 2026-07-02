### WAP to input angles of a triangle and check whether triangle is valid or not.

# Take input as interior angles of a triangle
angle_a = int(input('Enter 1st angle of a triangle : '))
angle_b = int(input('Enter 2nd angle of a triangle : '))
angle_c = int(input('Enter 3rd angle of a triangle : '))
angle_tri = angle_a + angle_b + angle_c

# operation with conditions
if (angle_tri == 180):
    print(f'TRIANGLE is valid.')
else:
    print('It\'s not a valid triangle.')

