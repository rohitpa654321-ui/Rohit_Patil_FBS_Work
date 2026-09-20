### Q. Write a program to find factorial using recursion.

def factNum(num):
    if num <= 1:
        return 1
    else:
        return num * factNum(num-1)
    
n = int(input('Enter number : '))
res = factNum(n)

print(f'Factorial of {n} = {res}')