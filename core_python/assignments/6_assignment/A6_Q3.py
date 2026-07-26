### Write a program print following patterns:


#     1
#    1 1
#   1 2 1
#  1 3 3 1


  
num  = 4

for i in range(num):
    val = 1
    for j in range(num-i):
        print(' ',end='')
        
    for j in range(i+1):
        # if (val<10):
        print(val,end =' ')
        # else:
        #   @@print(val, end='')
        val = val*(i-j) // (j+1)
    print()

    