###

n = int(input('Enter number : '))
a = -1
b = 1
if (n<600):
    for i in range(1,n):
        c = a+b
        a = b
        b = c
        print(c)
