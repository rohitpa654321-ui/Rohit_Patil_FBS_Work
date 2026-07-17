### Fabonacci series
num = int(input('Enter number : '))
n = 0
a = -1
b = 1

print('Fibonacci Series : ',end =' ')
while(n <= num):
      c = a+b
      print(f'{c}',end = ' ' )
      a = b
      b = c
      n+=1
      