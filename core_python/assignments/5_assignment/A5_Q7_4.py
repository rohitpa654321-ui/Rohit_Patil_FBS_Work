### d. S = a + a2 / 2 + a3 / 3 + ... + a10 / 10

n = int(input('Enter number (n) : '))
a = float(input('Enter a : '))
# term = 0
sum = 0
for i in range (1,n+1):
    
    # term = a*i/i
    sum = sum + a
    print(a)

print(f'Sum of given series : {sum}')


# ## optimising code by eliminating or reduced one variable use