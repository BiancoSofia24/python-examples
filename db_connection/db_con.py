import pymysql

"""
Create connection to the database
:param: none
:return: none
"""
def connect():
    return pymysql.connect(
        host="localhost", 
        user="root", 
        password="", 
        database="pythontestdb",
        charset="utf8mb4")

conn = connect()
cursor = conn.cursor()

"""
Get database version
:param: none
:return: none
"""
def db_version():
    cursor.execute("SELECT VERSION()")
    data = cursor.fetchone()
    print(f"Database version: {data}")

"""
Finding all the records in the table and fetching one by one
:param: none
:return: none
"""
def find_all():
    sql = "SELECT * FROM users"
    cursor.execute(sql)
    rows = cursor.fetchall()

    print("INFO: Finding all")
    print("ID | NAME      | EMAIL")
    print("-------------------------------------")
    for row in rows:
        id = row[0]
        name = row[1]
        email = row[2]
        print(f" {id} | {name} | {email}")

"""
Add record to the table
:param: name, email
:return: none
"""
def add(val):
    sql = "INSERT INTO users (name, email) VALUES (%s, %s)"
    try:
        cursor.executemany(sql, val)
        conn.commit()
        print("INFO: New record inserted")
    except Exception as e:
        conn.rollback()
        print(e)

# NOT WORKING
def find_by_id(id):
    sql = "SELECT * FROM users WHERE id = {0}".format(id)
    cursor.execute(sql)
    if cursor.fetchone() != None:
        record = cursor.fetchone()
        print(record)
    else:
        raise Exception(f"ERROR: Record not found with the id = {id}")

"""
Update record from the table
:param: id, name, email
:return: none
"""
def update(id, name, email):
    sql = "UPDATE users SET name = %s, email = %s WHERE id = %s"
    data = (name, email, id)
    try:
        cursor.execute(sql, data)
        conn.commit()
        print("INFO: Record updated")
    except Exception as e:
        conn.rollback()
        print(e)

"""
Delete record from the table
:param: id, name, email
:return: none
"""
def delete(id):
    sql = "DELETE FROM users WHERE id = {0}".format(id)
    try:
        cursor.execute(sql)
        conn.commit()
        print("INFO: Record deleted")
    except Exception as e:
        conn.rollback()
        print(e)

"""
Reset table by droping it and re creating
:param: none
:return: none
"""
def reboot():
    print("INFO: RESETING TABLE")
    sql = "DROP TABLE users"
    cursor.execute(sql)
    create_table()

"""
Create table
:param: none
:return: none
"""
def create_table():
    print("INFO: Creating table 'users'")
    sql = "CREATE TABLE IF NOT EXISTS users(id int(11) NOT NULL AUTO_INCREMENT, name TEXT NOT NULL, email TEXT NOT NULL, PRIMARY KEY(id)) ENGINE=InnoDB"
    cursor.execute(sql)
    conn.close()

"""
Add records to the table
:param: none
:return: none
"""
def fill_table():
    print("INFO: SETTING RECORDS")
    val = [
        ("Lucia", "lucia@mail.com"),
        ("Alejandra", "alejandra@mail.com"),
        ("Juan", "juan@mail.com")
    ]
    add(val)

def run_app():
    fill_table()
    find_all()
    update(3, "Jose", "jose@mail.com")
    val = [("Franz", "franz@mail.com")]
    add(val)
    find_all()
    delete(4)
    find_all()
    reboot()

run_app()