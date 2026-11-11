### trying to use with closing

import mysql.connector
from contextlib import closing

## trying for automatically closing connection
 
with closing(mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'rohit1234',
    database = ''
)) as conn:
    
    ## this is for auto close cursor
    # maintain intendation for with closing function
    with closing(conn.cursor()) as cur:
        queries = ['create database if not exists college',
        'use college',
        'create table if not exists student(id int primary key not null, name text not null)'
        ]
        
        for i in queries:
            cur.execute(i)
        conn.commit()
        
        cur.execute('describe student')
        print(cur.fetchall())
        
        