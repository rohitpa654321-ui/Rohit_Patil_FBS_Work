### Comparing length or size of genrator with list :

import sys                             # module import to use the function like getsizeof()

list = [i for i in range(1000000)]        

gen = (i for i in range(100000))

print(sys.getsizeof(list))          # size in bytes 
print(sys.getsizeof(gen))           

