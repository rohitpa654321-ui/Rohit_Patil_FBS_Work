### WAP to print Armstronge number within a given range.
n = int(input('Range starts : '))
m = int(input('Range ends (last neglect) : '))




for i in range(n,m):
    
    temp = i
    count = 0
    for j in range(1,i+1):
        if (temp>0):
            temp//=10
            count+=1
    
    temp = i
    sum = 0
    for j in range(1,i+1):
        if (temp>0):
            r = temp%10
            temp//=10
            sum = sum+r**count

    if (i == sum):
        print(i)
