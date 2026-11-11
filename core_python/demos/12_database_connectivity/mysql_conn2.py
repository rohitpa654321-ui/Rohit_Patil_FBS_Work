### mysql_connector

import mysql.connector

# connection to database :
try:
    conn = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'rohit1234',
        database = 'rg_practice'
    )
except Exception as e:
    print("! Database connection Problem : ",e)

# check database connection
if conn.is_connected():
    print('database connected successfully')
    
cur = conn.cursor()

## I have create new table :
cur.execute('create table if not exists emp(id integer primary key not null, ename text not null)')

## I just check can i describe table here or not
cur.execute('describe emp')
print(cur.fetchall())

## Insert records by id and name
# id = int(input("Enter emp id : "))
# name = input("Enter emp name : ")

# q = 'insert into emp(id, ename) values(%s,%s)'
# value = (id,name)

# cur.execute(q,value)
# conn.commit()

## update operation by firing query
qur = "update emp set ename = %s where id = %s"
change = [
    ('Mrunal Thakur',104),
    ('Sneha Sharma',105)
]
cur.executemany(qur,change)

## delete operation
qur = "delete from emp where id = %s"
dids = [
    (108,),
    (110,)
]
cur.executemany(qur,dids)
conn.commit()

# to see all records in table emp
cur.execute("select * from emp")
records = cur.fetchall()
# print(records)

for i in records:
    print(i)
        
cur.close()
conn.close()