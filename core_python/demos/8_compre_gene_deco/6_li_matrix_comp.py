### Comprehension : matrix as list in list (nested list) to access and print 
 
 
li = [[10,20],
      [30,40],
      [50,60]]

result = [x for i in li for x in i]
print(result)