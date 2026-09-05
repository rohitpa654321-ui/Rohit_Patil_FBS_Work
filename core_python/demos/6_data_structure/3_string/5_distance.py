### find distance with the string as characters given as direction

import math
path="WNEENSENNN"
x=0
y=0
for ch in path:
    if ch == 'N':
        y+=1
    elif ch == 'S':
        y -= 1
    elif ch == "E":
        x+=1
    elif ch == "W":
        x -= 1
# print(4 ** 0.5)
# dist=(x ** 2 +y ** 2) ** 0.5
dist=math.sqrt(x ** 2 +y ** 2)

print(f"The distence travled by the person in {path}= {dist}")