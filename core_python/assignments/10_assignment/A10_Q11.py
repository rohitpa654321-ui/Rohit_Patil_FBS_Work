### Q. Write a program to print all numbers which are divisible by m and n in the list.

li = [i for i in range(1,1000)]

m = int(input('Enter 1st Divisor : '))
n = int(input('Enter 2nd Divisor : '))

res = [i for i in li if (i % m == 0) and (i % n == 0)]

print(res)