

### Armstrong number detecting input given by user
no = int(input('Enter number:'))
temp = no
sum = 0
count = 0

while(temp > 0):
    count+=1
    temp= temp//10
print(count)
temp=no
while(temp>0):
    r = temp%10
    temp = temp // 10
    sum+= r**count
print(sum)
if (sum==no):
    print('Armstrong number : ',sum)
else:
    print('Not an Armstrong number.')

    