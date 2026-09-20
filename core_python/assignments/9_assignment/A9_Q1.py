### Write a program to find sum of following series using recursive functions.
# i.  1! + 2! + 3! + 4! + ... + n!

# Note :   For fact and sum two recursive functions.

def factR(n):
    fact = n
    if(n>0):
        return fact*factR(n-1)
    else:
        return 1


def factSum(n):
    
    sum = factR(n)
    
    if (n>0):
        return sum + factSum(n-1)
    else:
        return 0

print(f'Sum of Factorial Series : {factSum(5)}')