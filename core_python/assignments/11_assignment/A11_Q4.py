### Q. Python Program to Find the Second Largest Number in a List Using Bubble Sort.


li1 = [10,20,30,50,90,30,40,60]

def bubble_sort(li):
    for i in range(1,len(li)):
        for j in range(len(li)-1):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]

    return li[-2]

print(bubble_sort(li1))
