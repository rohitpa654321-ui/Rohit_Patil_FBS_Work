### Q.  Write a program to print list after removing even numbers.

li = [i for i in range(1,50)]

li_odd = [i for i in li if i%2!=0]

print(li_odd)