from sqlite3 import *
from sqlite3 import Error

def create_connection(path: str):
    """
    Ühendus andmebaasiga
    """
    connection = None
    try:
        connection = connect(path)
        print("Uhendus on edukalt tehtud")
    except Error as e:
        print(f"Tekkis viga '{e}'")
    return connection

def execute_query(connection, query: str):
    """Tabeli loomine"""
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        print("Tabel on loodud")
    except Error as e:
        print(f"Viga '{e}' tabeli loomisega")

def execute_read_query(connection, query: str):
    """Tabeli andmete vaatamine"""
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"Viga '{e}'")

def execute_delete_query(connection, query: str):
    """Tabeli/andmete eemaldamine"""
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        print("Tabel/andmed on kustutatud")
    except Error as e:
        print(f"Viga '{e}'")

# SQL laused--------------------------------------------------------------------------
create_users_table = """
CREATE TABLE IF NOT EXISTS users(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
age INTEGER,
gender TEXT,
student BOOLEAN
);
"""

create_users = """
INSERT INTO 
    users(name,age,gender,student)
VALUES
    ('Marti',45,'mees',false),
    ('Kadri',18,'naine',true),
    ('Andres',25,'mees',true),
    ('Mari',65,'naine',true),
    ('Anna',97,'naine',false);
"""

select_users = "SELECT * FROM users"

delete_data_from_users = "DELETE FROM users WHERE student = true"

delete_table_users = "DROP TABLE users"
# Kasutame----------------------------------------------------------------------------

con = create_connection("C:/Users/opilane/Desktop/TTHK/json_database/appData/data.db")

execute_query(con, create_users_table)

execute_query(con, create_users)

users = execute_read_query(con, select_users)
print("Kasutajate andmed:")
for user in users:
    print(user)

execute_delete_query(con,delete_data_from_users)
users = execute_read_query(con, select_users)
print("Kustutatud tudengid, on jaanud neid kellel student=0")
for user in users:
    print(user)

execute_read_query(con, delete_table_users)