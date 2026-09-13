### Sum of all odd numbers between 1 to n.

def oddSum(n):
    sum = 0
    for i in range(2,n+1):
        if (i%2!=0):
            sum+=i
    return sum

print(f'Sum of odd nummber series : {oddSum(int(input('Enter range (n) : ')))}')