### Q. Python Program to Merge Two Lists and Sort it.

li1 = [10,20,30,50,90,30,40,60]
li2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def mergeAndSort(li1,li2):
    li3 = li1 + li2

    for i in range(1,len(li3)):
        for j in range(len(li3)-1):
            if li3[j] > li3[j+1]:
                li3[j], li3[j+1] = li3[j+1],li3[j]
    return li3

print(mergeAndSort(li1,li2))