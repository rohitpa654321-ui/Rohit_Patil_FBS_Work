### Keyword parameter :

def emp(id,name,sal,dept):
    data = f' ID : {id} \nNAME : {name} \nSAL : {sal} \nDEPT : {dept}'
    return data

res = emp(1001, sal = 150000, name = 'Rohit', dept = 'AI')
print(res)

