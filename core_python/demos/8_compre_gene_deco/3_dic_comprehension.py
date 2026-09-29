### Dictionary comprehension : 

# Traditional
dic = {}
for i in range(1,10):
    dic[i]=i ** 2
print('Traditional = ',dic)

# Comprehention with dictionary
dic = {i:i*i for i in range(1,11)}
print('Comprehension',dic)


# Comprehension with string 

name = "Python"
result = (ch.upper() for ch in name)
print(list(result))