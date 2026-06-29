
### Numeric 

# 1. int 
x = 10
print(type(x))

# 2. float
x = 3.14
print(type(x))

# 3. complex
x = 4 + 10j      # Real + imaginary
print(type(x))



### Text
# 1. str
x = 'I am "Rohit" '
x = "I am 'Rohit' "

x = '''this 1st line
this is 2nd line'''

x = """this 1st line
this is 2nd line"""

print(type(x))


### Sequential

# 1. list
x = [10, 20, 30, 40]
print(type(x))

# 2. tuple
x = (1,2,3,4,34)
print(type(x))

# 3. range
x = range(1,10)
print(type(x))

### Set type

# 1. set
x = {1,2,45,34,20}
print(type(x))

# 2. frozenset
x = frozenset({12,13,14,15,16})

print(type(x))

### Mapping
# 1. dict
x = {1 : "python", 2: "Java", 3: "c", 4: "R" }
print(x)

### Other
# 1. boolen type
x = 10
y = bool(x)
print(y)

x = True
x =  False

# 2. Nonetype

x = None
print(type(x), x)