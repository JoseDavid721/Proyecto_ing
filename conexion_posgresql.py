#Proyecto_ing
import psycopg2

try:
    connection = psycopg2.connect(
        host='localhost',
        user='postgres',
        password='123456789',
        database='proyecto'
    )
    print('Conexión exitosa')
    cursor = connection.cursor()
    cursor.execute("SELECT version()")
    row = cursor.fetchone()
    print(row)
    cursor.execute("SELECT * FROM Medicamento")
    rows=cursor.fetchall()
    for row in rows:
        print(row)
except Exception as ex:
    print(ex)
