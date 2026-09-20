### Q. Write a program to check whether a number is prime or not using recursion. 

def primeCheck(num, n = 2):
    
    if num <= 1:
        return 'Not a Prime Number'
    if n > num ** 0.5:
        return  'Prime Number'
    if num % n == 0:
        return 'Not a Prime Number'
    
    return primeCheck(num,n+1)

res = primeCheck(num = int(input('Enter Number : ')))

print(res)