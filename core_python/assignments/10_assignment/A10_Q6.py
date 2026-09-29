### Q. Write a program to remove duplicates from the list. 

li = [1,2,1,4,8,2,5,3,9,6,7,3,4,5,9,6,7,1,8]

s1 = set(li)
li = list(s1)
print(li)

### If I use loop... complexity will increase in code

# un = []

# for i in li:
#     if i not in un:
#         un.append(i)

# print(un)