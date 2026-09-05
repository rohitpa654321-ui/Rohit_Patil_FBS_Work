### To find Second Max number in list.

li = [34,87,56,23,76,12,67,98]

max1 = 0
max2 = 0

for i in range(len(li)):
    if (li[i] > max1) :
        max2 = max1
        max1 = li[i]

print(max2)