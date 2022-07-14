""" Conectarse a una base de Datos MySQL"""
import mysql.connector

base = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "D3mon1o.",
    database = "abacom"
)

cursor = base.cursor()
cursor.execute('select * from Usuario')

resultado = cursor.fetchall()

print(resultado)