### Q. Python Program to Find the Intersection of Two Lists.

li1 = [21,22,23,24,25]
li2 = [21,24,26,27,28]

li_in = list(set(li1) & set(li2))

print(li_in)