### Write a program to find the second largest element in the list.


li = [10,20,30,50,90,30,70,40,60]

max = 0
smax = 0

for i in li:
    for j in li:
        
        for k in range(1,len(li)):
            for l in range(len(li)-1):
                if li[l] > li[l+1]:
                    li[l],li[l+1]=li[l+1],li[l]                
            
    if max < i:
        smax,max = max,i
        
print(f'Second largest element = {smax}')