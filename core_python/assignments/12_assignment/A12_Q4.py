### Q. Python Program to Form a New String where the First Character and 
#      the Last Character have been Exchanged

str1 = 'PythoN'
str2 = 'DNA'

str1 = str1[-1] + str1[1:-1] + str1[0]
str2 = str2[-1] + str2[1:-1] + str2[0]

print(str1 , str2 , sep = '\n')