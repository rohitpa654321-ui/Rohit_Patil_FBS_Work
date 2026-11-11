### Q. Python Program to Count the Frequency of Words Appearing in a String Using a Dictionary.

dic = {}
str = input('Enter String : ')

word = str.split()

for i in word:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
    
print(dic)