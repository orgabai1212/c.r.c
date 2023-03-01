import mysql.connector
def connect():
    return mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="crc",
    port="3306"
    )

def sql_command(command):
    conection =connect()
    cursor = conection.cursor()
    cursor.execute(command)
    result=cursor.fetchall()
    cursor.close()
    conection.close()
    return result

def sql_insert(id,first_name,last_name):
    conection =connect()
    cursor = conection.cursor()
    qury="insert into employees (id,first_name,last_name) values (%s,%s,%s)"
    values=(id,first_name,last_name)
    cursor.execute(qury,values)
    conection.commit()
    cursor.close()
    conection.close()
    
sql_insert('1234567','nofar','bar')
m="""
select * from employees;
"""



q=sql_command(m)
print(q)
