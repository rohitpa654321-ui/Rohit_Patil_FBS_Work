### Write a program to find print the following fibonacci series using
# function:    1 1 2 3 5 8 ... n term
# as per question
def fibonacciS(n):
    a = 1
    b = 0
    for i in range(1,n):
        c = a+b
        a = b
        b = c
        print(c)
    return 'end'
    
print(fibonacciS(int(input('Enter number (n) : '))))


# for original fibonacci series

def fibonacciS(n):
    a = -1
    b = 1
    for i in range(1,n):
        c = a+b
        a = b
        b = c
        print(c)
    return 'end'
    
print('\nOriginal fibonacci series')
print(fibonacciS(int(input('Enter number(n) : '))))

