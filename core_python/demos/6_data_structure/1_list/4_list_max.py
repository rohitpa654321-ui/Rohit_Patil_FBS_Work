### maximum number in list :

li = [34,23,32,46,67,73,26,24,87]

max = li[0]

for i in range(1,len(li)):
    if (li[i]>max):
        max = li[i]
    
print('MAX is : ',max)
