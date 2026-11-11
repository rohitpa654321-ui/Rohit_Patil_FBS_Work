### Q. Python Program to Generate a Dictionary that Contains Numbers (between 1 and n) in the Form (x,x*x).

dic = {}

n = int(input("Enter the key range : "))

for i in range(1,n+1):
    dic[i] = i*i
    
print(dic)