### Q. Write a program to calculate the m to the power n using recursion. 

def powerOf(m,n):
    if n == 0:
        return 1
    else:
        return m * powerOf(m,n-1)

res = powerOf(int(input('Enter number m : ')),int(input('Enter number n : ')))

print(res)