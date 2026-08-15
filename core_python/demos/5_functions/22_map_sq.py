### maping function : square of elements in data

def sq(num):
    return num**2

data = [10,20,30,40,50,60,70,80,90]

res = list(map(sq,data))

print(res)
