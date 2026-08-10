### function :  Armstrong number check

def isArmstrong(num):
    sum = 0
    temp = num
    count = 0
    while(temp>0):
        temp//=10
        count+=1
    temp = num
    while(temp > 0):
        sum = sum + (temp%10)**count
        temp//=10
    if (sum == num):
        return 1
    else:
        return 0
    
num = int(input('Enter number : '))
res = isArmstrong(num)
if (res):
    print('Yes Armstrong number.')
else:
    print('Not Armstrong number.')