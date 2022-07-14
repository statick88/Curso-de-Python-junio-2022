""" Conectarse a una base de Datos MySQL"""
import mysql.connector

base = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "D3mon1o.",
    database = "abacom"
)

#Lista Datos
cursor = base.cursor()
# cursor.execute('select * from Usuario')
# resultado = cursor.fetchall()
# print(resultado)

# cursor.execute('select * from Usuario limit 1')
cursor.execute('select * from Usuario limit 2')
resultado = cursor.fetchall()
print(resultado)

#Ver definiciones de tablas
#cursor.execute('show create table Usuario')

#Insertar datos
#sql = "insert into Usuario (email, username, edad) values (%s, %s, %s)"
#values = ('micorreo@gmail.com', 'nombredeusuario',45)
#cursor.execute(sql, values)
#base.commit()

#Actualizar datos 
#sql = "update Usuario set email = %s where id = %s"
#values = ('micorreomodificado@gmail.com','4')
# cursor.execute(sql, values)
# base.commit()

# sql = 'delete from Usuario where id =%s'
# values = (4,)
# cursor.execute(sql, values)
# base.commit()