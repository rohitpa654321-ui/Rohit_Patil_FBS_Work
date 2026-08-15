### Sum of digit :

def digiSum(num):
    
    d = num%10
    
    if (num>0):
        return d + digiSum(num//10)
    
    return 0

res = digiSum(int(input('Enter number : ')))
print('Sum of Digit is  : ',res)