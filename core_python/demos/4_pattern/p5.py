### pattern : 

#  1
#  1 2
#  1 2 3
#  1 2 3 4
#  1 2 3 4 5


#  increase column range with same value in column

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end =' ')
        j+=1
    print()
    