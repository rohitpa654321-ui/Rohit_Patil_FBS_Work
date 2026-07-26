### e. x - x2/3 + x3/5 - x4/7 +... to n terms 

n = int(input('Enter number (n) : '))
x= int(input('Enter x value : '))
# k = 0
sum = 0
for i in range (1, n+1):
    # k = i+(i-1)      
    # for j in range(k,k+1):
    #     print(j)
    # sum =(x*i/i+i-1)
    # c = (x*i)/(i+i-1)
    # s = x*i / (i+i-1)
    if (i%2==0):
         sum = sum - (x*i / (2*i-1))
         print(f'{x}*{i}/{i+i-1}', f'= -{(x*i / (2*i-1))}')
    else:
        sum = sum + (x*i / (2*i-1))
        print(f'{x}*{i}/{i+i-1}', f'= {(x*i / (2*i-1))}')
print(f'Sum of series is : {sum}')

### Optimise the the program as follow:
# reduce unnecessary part as loop for j make slower the program and some variables.
# implementing branching for better decision.