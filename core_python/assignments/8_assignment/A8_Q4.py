### Write program to find sum of following series using function:
# b.  1! + 2! + 3! + 4! +... + n!

def factSum(n):
    sum = 0
    fact = 1
    
    for i in range(1,n+1):
        fact = fact*i
    sum += fact 
    fact = 1
    
    return sum

print(f'Sum of factorial : {factSum(int(input('Enter number : ')))}')