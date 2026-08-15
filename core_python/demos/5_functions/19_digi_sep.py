### Digit Seperation function :

def digSep(num):
    if(num>0):
        print(num%10)
        digSep(num//10)


digSep(int(input('Enter number : ')))
