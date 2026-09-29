### Nested list comprehention :

result = [x*y for x in [1,2,3] for y in [10,20]]
print("Nested : ",result)


### list comprehension with if else:  

marks = [90,75,45,25]

res = ["A" if mark>=80 else "B" if mark >=60 else "C" if mark>= 40 else "Fail" for mark in marks]
print("with if else : ",res)
