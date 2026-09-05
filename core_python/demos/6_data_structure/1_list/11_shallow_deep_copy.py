### Shallow and deep Copy : 

import copy

# Shallow copy :

original = [[1, 2], [3, 4]]

shallow = copy.copy(original)

shallow[0][0] = 100

print("Shallow copy original list : ",original)
print("Shallow copyed list : ",shallow)


print('\n')
### Deep copy :
original = [[1, 2], [3, 4]]             # nested list

deep = copy.deepcopy(original)

deep[0][0] = 100
deep.append([12,21])

print( "Deep copy original list : ", original)
print("Deep copyed list : ", deep)