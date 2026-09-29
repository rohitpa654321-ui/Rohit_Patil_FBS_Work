### Q. Write a program to remove all occurrences of a given element in the list.

li = [1,2,5,7,1,3,4,1,1,2,6,4,7,2,7,7,5,2]
ele = int(input('Enter Element to remove : '))

li = [i for i in li if i != ele]


# for i in li:
#     if i == ele:
#         li.remove(i)


print(li)