### generator example :

def count(n):
    for i in range(1,n+1):
        yield i
        

for num in count(5):      # loop act as next to generate value
    print(num)
        
        
# print(list(map(lambda x : x , count(5))))   

# gen = list(map(lambda x : x , count(5)))
# print(gen)