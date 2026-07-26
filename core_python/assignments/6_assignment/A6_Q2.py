### Write a program print following patterns:

#   1
#   2 3
#   4 5 6
#   7 8 9 10

k = 1
for i in range(1,5):
    for j in range(i,i*2):
        print(k,end=' ')
        k+=1
    print()