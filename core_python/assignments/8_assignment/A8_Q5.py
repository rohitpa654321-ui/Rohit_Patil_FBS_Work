### Write a program to find sum of following series using function :
#  c.  1^1 + 2^2 + 3^3 + 4^4 + ... + n^n

def seriesSum(n):
    sum = 0
    for i in range(1,n+1):
        sum = sum + i**i
    return sum

print(f'Sum of series : {seriesSum(int(input("Enter n : ")))}')