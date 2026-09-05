### Selection Sort

def selectionSort(li):
    size = len(li)
    for i in range(0,size-1):
        min_ind = i
        for j in range(i+1, size):
            if (li[min_ind] > li[j]):
                min_ind = j
                
        li[i],li[min_ind] = li[min_ind],li[i]
        print(li)
    
li = [60,50,40,30,20,10]
print("Original list : ",li)
selectionSort(li)
# print('After Sorting : ',li)

print("\n\n....................................................................\n")

li2 = [60,30,20,10,50,40]
print("Original list : ",li2)
selectionSort(li2)
# print('After Sorting : ',li)

