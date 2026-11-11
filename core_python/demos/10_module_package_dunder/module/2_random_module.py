# ### Random module

import random

print(random.random())                   # Random float 0 to 1

print(random.randint(1, 10))             # Random integer 1-10

print(random.randrange(1,10,2))           # Random number from range   random.randrange(start,stop,step)

print(random.choice([10,20,30]))         # Select one item

print(random.choices([1,2,3], k=2))      # Select multiple, repetition possible  and k = number of output

print(random.sample([1,2,3,4], 2))       # Select multiple, no repetition

li = [5,3,2,6,1,7,5,3]
print(random. shuffle(li))               # Randomly rearranges list
print(li)

print(random.uniform(1, 10))             # Random float between 1-10