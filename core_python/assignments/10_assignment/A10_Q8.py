### Q. Write a program to create a duplicate of an existing list. It should not point to 
#      same list.

import copy

li = [[10,20,[50,40]],30,50,90,30,70,40,60]

# li2 = copy.copy(li)
li2 = copy.deepcopy(li)

li2[0][2][0]= 12
li2[0][0] = 70

print(li2)
print(li)