### Write a program to find sum of n numbers using recursion.

def sumN(n):  
    if n == 0:
        return 0
    else:
        return n + sumN(n-1)


n = int(input("Enter number : "))
result = sumN(n)
print(f'Sum = {result}')