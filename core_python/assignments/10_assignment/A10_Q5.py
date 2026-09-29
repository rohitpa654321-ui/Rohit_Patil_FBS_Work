###  Accept a number from user and check if this element is present in the list or 
#    not. Also tell how many times it is present in the list.

li = [1,2,1,4,8,2,5,3,9,6,7,3,4,5,9,6,7,1,8]

def searchEle(list, el):
    count = 0
    for i in li:
        if i == el:
            count += 1
        
    if count > 0:
        print(f'Element Found : {count} times ')
        
    else:
        print('Element Not Present in List')
    
    
searchEle(li, int(input('Enter Element to search : ')))