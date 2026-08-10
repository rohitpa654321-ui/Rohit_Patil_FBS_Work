### different two function as Factorial and strong.

def factorialOf(n):
    fact = 1
    temp = n
    while(temp>1):
        fact = fact*temp
        temp-=1 
    return fact

def isStrong(num):
    tem = num
    sum = 0
    while(tem>0):
        d = tem%10
        sum = sum + factorialOf(d)
        tem//=10
    
    if (sum == num):
        return 1
    else:
        return 0
    
x = int(input('Enter number : '))

res = isStrong(x)

if(res):
    print('Yes Strong number.')
else:
    print('Not Strong number.')