### Sum of all prime numbers between 1 to n .

def sumPrime(n):
    sum=0
    for i in range(2,n+1):
        req=1
        for j in range(2,i):
            if (i%j==0):
                req=0
        if (req):
            print(i)
            sum+=i
    return sum


print(f'Sum prime numbers : {sumPrime(int(input('Enter range(n) : ')))}')