### Q. Write a program to create a new list from existing list which contains cube of 
#   each number of list. 


li = [1, 2, 3, 4, 5, 6, 7, 8, 9]

li_cube = [i**3 for i in li]

print(li_cube)