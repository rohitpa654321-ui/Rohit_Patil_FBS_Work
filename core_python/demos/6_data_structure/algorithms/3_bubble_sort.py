### Bubble Sort

def bubbleSort(li):
    size = len(li)
    for i in range(1,size):
        for j in range(0,size-1):
            if(li[j] > li[j+1]):
                li[j],li[j+1] = li[j+1], li[j]
                print(li)

li = [40,10,30,20,50,60]
print("original list",li)
bubbleSort(li)

print("\n\n..........................................................................\n")

li = [60,50,40,30,20,10]
print("original list",li)
bubbleSort(li)
