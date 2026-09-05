### Dictionary : lists stored in dictionary

emp={}
for i in range(1,4):
    name=input(f"Enter the name of {i}th Employee ")
    sal=float(input(f"Enter the Sal of {i}th Employee "))
    address=input(f"Enter the Address of {i} th Employee =")
#   emp[i]={'name':name,"salary":sal,"addrss":address}
    emp[i]=[name,sal,address]
    
print(emp)
