### Q. Write a program to print list after removing even numbers.

li = [i for i in range(50,100)]

li = [i for i in li if i % 2 != 0]

# for i in li:
#     if i % 2 == 0:
#        li.remove(i) 

print(li)