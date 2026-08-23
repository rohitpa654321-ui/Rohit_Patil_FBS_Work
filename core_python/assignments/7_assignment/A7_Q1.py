### Write a program to print following pattern:

#      *
#     * *
#    *   *
#   *     *
#  *       *
#  *       *
#   *     *
#    *   *
#     * *
#      *


for i in range(1,6):

    for j in range(1,6-i):
        print(end=' ')
        
    for j in range(1,2*i):
        if(j==1 or j==2*i-1):
            print('*',end='')
        else:
            print(' ',end='')
    print()
for i in range(1,6):
    for j in range(1,i):
        print(' ',end='')
    for j in range(1,12-i*2):
        if ( j==1 or j==12-i*2-1):
            print('*',end='')
        else:
            print(' ',end='')
            
    print()