### Q. Python Program to Put Even and Odd elements of a List into two Different Lists.

li = [i for i in range(1,50)]

even = []
odd = []

for i in li:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print("Even list : ", even)
print("Odd list : ", odd)