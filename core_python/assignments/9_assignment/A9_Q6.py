### Write a program to print Fibonacci series using recursion.


def fibonacciS(n):
    
    if n <= 1:
        return n
    else:
        return fibonacciS(n - 1) + fibonacciS(n - 2)
    

ranges = int(input('Enter range of fibonacci series : '))

for i in range(ranges):
    print(fibonacciS(i))