### Write a program to check if number is positive or negative

# Take input 
num = int(input('Enter number : '))

# conditional operation
if (num > 0):
    print('Given number is positive .')
elif (num == 0):
    print('Given number is nuetral .')
elif (num <= 0):
    print('Given number is negative .')
else :
    print('incorrect value...')