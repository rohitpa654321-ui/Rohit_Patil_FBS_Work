### Write a program print following patterns:

#          1
#        2 3 2
#      3 4 5 4 3
#    4 5 6 7 6 5 4
#  5 6 7 8 9 8 7 6 5


for i in range(1,6):
    
    for j in range(1,6-i):
        print(' ', end=' ')
        
    for j in range(0,i):
        print(j+i, end=' ')
        
    for j in range(i-1,0,-1):
        print(j+i-1,end=' ')


    print()
    