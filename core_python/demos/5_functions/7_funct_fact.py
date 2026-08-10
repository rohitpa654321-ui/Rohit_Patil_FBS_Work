### Is strong nummber or not

def factorial(num):
    fact = 1
    while(num>0):
        fact = fact * num
        num-=1
    return fact
        

fact = factorial(int(input('Enter number : ')))
print(fact)


