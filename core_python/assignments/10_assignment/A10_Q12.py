### Q. Write a program to create three lists of numbers, their squares and cubes.

li = [i for i in range(1,25)]
li_sq = [i**2 for i in li]
li_cube = [i**3 for i in li]

print (li)
print (li_sq)
print (li_cube)
