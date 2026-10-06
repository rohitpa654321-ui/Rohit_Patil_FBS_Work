### Q. Print 1 to 100 in snakes and ladder pattern.

n = 1

for i in range(10):
    num = list(range(n,n+10))
    
    
    if i % 2 == 0:
        num.reverse()
        
    print(num)
    n+=10
    
    