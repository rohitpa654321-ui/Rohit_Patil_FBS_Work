### Practice pattern :

#   1 _ _ _ _ _ _ _ 1
#   1 2 _ _ _ _ _ 2 1
#   1 2 3 _ _ _ 3 2 1
#   1 2 3 4 _ 4 3 2 1
#   1 2 3 4 5 4 3 2 1

k = 7

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end= ' ')
    for j in range(1,k+1):
        print('_', end = ' ')
    k-=2
    for j in range(i,0,-1):
        if (j != 5):
            print(j,end = ' ')
    print()
    
    