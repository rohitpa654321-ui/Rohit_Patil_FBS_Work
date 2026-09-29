### Example and practice for generator

from time import sleep     # import function sleep from time to delay runtime to understand code

def gen(n):                      
    for i in range(1,n+1):
        yield(i)
        
g = gen(5)

print(next(g))
print("just stop") 
# sleep(2)                         # sleep is used to delay the run time by 2 seconds
print(next(g))
print("let's the next nummber come")
# sleep(2)
print(next(g))
print("my number came")
# sleep(2)
print(next(g))
print(next(g))