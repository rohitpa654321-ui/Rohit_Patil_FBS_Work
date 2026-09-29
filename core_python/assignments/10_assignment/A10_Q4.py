### Q. Write a program to reverse the list.


li = [10,20,30,50,90,30,40,60]

mid = len(li)//2
for i in range(mid):
    li[i],li[-i-1]=li[-i-1],li[i]


print(li)