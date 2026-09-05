### input elements from user.

def createList(li):
    n = int(input('Enter number of element to add : '))
    
    for i in range(n):
        el = int(input('Enter element : '))
        li.append(el)
    
li = []
createList(li)     # mutability
print(li)          # without returning val it make change in original li