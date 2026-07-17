### Write a program to print all even number until n.

num = int(input('Enter number : '))
n = 1
while (n<=num):
    if (n % 2 == 0):
        print(n)
    n+=1
