### seperate out digits

num = int(input('Enter number :'))
temp = num
count =0
while (temp > 0):
    r = temp % 10
    temp = temp // 10
    print(r)
    print(temp)
    count += 1
    
print('Total count :',count) 