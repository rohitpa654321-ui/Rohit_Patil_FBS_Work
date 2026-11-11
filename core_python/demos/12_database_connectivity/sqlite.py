import sqlite3

conn = sqlite3.connect('rg_practice.db')

print(conn)
print("Database created and Successfully Connected to SQLite")

cur = conn.cursor()

cur.execute("""
    create table if not exists employee (
        emp_id integer primary key,
        emp_name text not null,
        age integer,
        gender text,
        department text,
        salary decimal (10,2),
        city text,
        joining_date text
    )
""")

# employees = [
#     ("Rahul", 25, "Male", "IT", 45000, "Pune", "2025-06-15"),
#     ("Priya", 24, "Female", "HR", 40000, "Nashik", "2025-07-10"),
#     ("Amit", 27, "Male", "Finance", 50000, "Mumbai", "2025-08-01")
# ]

# cur.executemany("""
#     inset into employee
#     (emp_id,emp_name, age, gender, department, salary, city, joining_date)
#     values (?, ?, ?, ?, ?, ?, ?)
# """, employees)

# conn.commit()

cur.execute('select * from employee')

row = cur.fetchall()

for i in row:
    print(i)