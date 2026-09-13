### Write a program to check if entered year is a leaf year or not.

def leafYear(year):
    if (year>999 and year<9999):
        if (year % 4 ==0):
            return 'Leaf year'
        else:
            return 'NOT leaf year'
    else:
        return 'Invalid !'
    
print(leafYear(int(input('Enter year(4 digit) : '))))