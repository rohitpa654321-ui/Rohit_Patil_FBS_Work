### Q. Write a program of having n number of elements in the list and find out even 
#      and odd elements in that list and then create two separate lists which will have 
#      even elements and other will have odd elements.

li = [i for i in range(1,int(input('Enter n :'))+1)]

li_even = [i for i in li if i % 2 == 0]
li_odd = [i for i in li if i % 2 != 0]

print(f'Even Element List : {li_even}')

print('\n\n.................................................................................\n\n')

print(f'Odd Element List : {li_odd}')