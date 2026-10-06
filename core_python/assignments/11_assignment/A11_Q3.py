### Q. Python Program to Sort the List According to the Second Element in Sublist

list = [['Laptop', 1200], ['Mouse', 25], ['Keyboard', 75], ['Monitor', 300]]

list.sort(key = lambda x : x[1])

# def sort_sec(li):
#     for i in range(1,len(li)):
#         for j in range(len(li)-1):
#             if li[j][1] > li[j+1][1]:
#                 li[j], li[j+1] = li[j+1], li[j]

#     return li

# print(sort_sec(list))

print(list)