### Q. Python Program to Sort a List According to the Length of the Elements within the list.

li = ['apple', 'coconut','banana','berry','almond','apple','kiwi','dragonfruit','Pineapple']

for i in range(1,len(li)):
    for j in range(len(li)-1):
        if len(li[j]) > len(li[j+1]):
            li[j],li[j+1] = li[j+1], li[j]

print(li)

