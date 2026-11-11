### Q. Python Program to Add a Key-Value Pair to the Dictionary

dic = {}
i=1

while i >= 1 :
    key  = input("Enter key : ")
    value = input("Enter value for Key : ")

    dic[key] = value
    i = int(input("to add (1) and exit (0) : "))

print(f'Dictionary : {dic}')