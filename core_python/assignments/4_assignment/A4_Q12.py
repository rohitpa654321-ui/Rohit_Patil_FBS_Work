### Write program to check the given no is armstrong number or not. 

num = int(input('Enter number : '))
temp = num
tem = num
count = 0
sum = 0

while (temp>0):
    
    while(tem>0):
        tem//=10
        count+=1
    
    r = temp%10
    temp = temp//10
    sum = sum + r**count
    
if (num == sum):
    print(f'{num} is an Armstrong number.')
    
else:
    print(f'{num} is NOT an armstrong number.')
    
