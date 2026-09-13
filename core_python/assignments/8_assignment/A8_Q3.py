### write program to find sum of following series using function.
#  a. 1+2+3+4+...+n

def seriesSum(n,sum=0):
    for i in range(1,n+1):
        sum+=i
    return sum

print(f'Sum of series : {seriesSum(9)}')
