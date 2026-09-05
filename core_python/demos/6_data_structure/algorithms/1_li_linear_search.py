li = [10,20,30,40,53,50,34,23,4,5]


def linearSearch(li,element):
    
    for i in range(0,len(li)):
        if(li[i] == element):
            return f'Element found at index : {i}'
    else:
        return 'NOT found'
        
print(linearSearch(li,int(input('Enter element for search : '))))
