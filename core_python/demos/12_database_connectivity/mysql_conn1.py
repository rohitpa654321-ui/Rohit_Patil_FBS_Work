### mysql-connector-python



import mysql.connector

try:
    con = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'rohit1234',
        database = 'rg_practice'
)
except Exception as e:
    print("! Database connection Problem : ",e)

if con.is_connected() == True:
    print('Databases connected successfully')

cur = con.cursor()
q = 'select * from employee'
# quary = "insert into employee values(%s,%s,%s,%s,%s,%s,%s)"
# quary = "insert into employee values(12,'narayan',24,'Male','HR', 45000,'Nagar' )"


# values = (11,'mayank',23,'Male','Marketing',35000,'Nagpur')

# cur.execute(quary)               
# con.commit()
cur.execute(q)


records = cur.fetchone()
print(records)

records = cur.fetchmany(3)
# records = cur.fetchall()

for i in records:
    print(i)
    
cur.close()
con.close()