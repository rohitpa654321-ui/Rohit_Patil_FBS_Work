### Q. Write a program to create three lists of numbers, their squares and cubes.

li = [i*3 for i in range(1,20)]
li_sq = [i**2 for i in li]
li_cube = [i**3 for i in li]

print(li,li_sq,li_cube, sep = "\n")