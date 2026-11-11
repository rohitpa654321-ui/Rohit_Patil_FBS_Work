### Pickling is a way to convert a Python object into a byte stream.

# pickle.dump()

### Unpickling is the inverse operation, converting a byte stream back into a Python object.

# pickle.load()

### This is useful for saving complex data structures to a file or sending them over a network.


import pickle
from emp import Emp

e1 = Emp(21,"Rohit", 75000)

with open("11_file_handling/emp.txt", 'ab') as f:
    pickle.dump(e1,f)
    pickle.dump(Emp(22,"Ram", 80000),f)
    
with open("11_file_handling/emp.txt", 'rb+') as f:
    d = pickle.load(f)     # first dump object is loaded
    a = pickle.load(f)     # second dump object will be loaded
    # error = pickle.load(f)  # This will raise an EOFError since there are only two objects in the file
print(d)
print(a)

