### c. Find the sum of a geometric series from 1 to n where the common ratio is 2.  

n = int(input('Enter number (n) : '))
sum = 0
g = 1
for i in range(1,n+1):
    i = g
    g = 2*i
    sum = sum + g
    print(f'{g} ')
print(f'Sum og geometric series : {sum}')
