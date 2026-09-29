### Comprehension in python : concise way to create collections.
# supports or include list, set, dictionary, generator
# uses for and optional condition.

# list comprehension
li = [i+i for i in range(1,11)]  # [expression for item in iterable]
print('list = ',li)

# set comprenhension
number = [1,3,1,2,4,5,2]
unique = {x for x in number}
print('set-Unique = ',unique)

# Dictionary comprehension
squares = {x: x*x for x in range(1, 6)}
print('Dic-sq = ',squares)

# Generator comprehension - denot simply by ()
numbers = (x*x for x in range(5))
print(f'generator-num = { list(numbers)}')