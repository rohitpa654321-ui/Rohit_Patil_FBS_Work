### prime number upto 100
# 1 is not a Prime and composite number
num = int(input('Enter number : '))

for i in range(2,num):
    for j in range(2,i):
        if (i % j != 0 ):
            continue
        else:
            break
    else:
        print(i)
            