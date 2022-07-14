import mysql.connector

midb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="D3mon1o.",
    database="abacom"
)

cursor = midb.cursor()

cursor.execute('select * from Usuario;')

resultado = cursor.fetchall()

print(resultado)