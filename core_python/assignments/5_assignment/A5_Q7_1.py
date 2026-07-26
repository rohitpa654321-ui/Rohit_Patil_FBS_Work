### 7. Write a program to solve the following series : 
### 7.1 a. 1! + 2! + 3! + 4! + ...n!  
# 7.2 b. N + N^2 + N^3+N^4 ... +N^N (here ^ means exponent)  
# 7.3 c. Find the sum of a geometric series from 1 to n where the common ratio is 2.  
# 7.4 d. S = a + a2 / 2 + a3 / 3 + ... + a10 / 10  
# 7.5 e. x - x2/3 + x3/5 - x4/7 +... to n terms 


### 7.1 a.  1! + 2! + 3! + 4! + ... n!  

n = int(input('Enter number (n) :'))
sum = 0
for i in range(1,n+1):
    
    fact = 1
    for j in range(1,i+1):
        fact*=j
    sum += fact
    
print('Series solution is : ',sum)