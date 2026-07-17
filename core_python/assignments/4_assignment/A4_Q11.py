### WAP to check if given number is strong number. 

num = int(input('Enter number : '))
temp = num
sum = 0

while(temp>0):
    fact = 1
    r = temp%10
    temp = temp//10
    
    while (r>0):
        fact = fact*r
        r-=1
    sum+=fact
    
if (num == sum):
    print(f'{num} is a Strong number.')
else:
    print(f'{num} is NOT strong number.')