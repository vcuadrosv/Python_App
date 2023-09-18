'''
Primero se establece la conexion a la base de datos por lo tanto, se instala el siguiente comando

    pip install mysql-connector-python

El motivo de instalar el módulo mysql-connector-python es que proporciona las herramientas necesarias para que una 
aplicación Python pueda comunicarse de manera eficiente con una base de datos MySQL. 

'''

import mysql.connector

# Se establece la conexión a la base de datos
conexion = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Artes2021*",
    database="conection"
)

# Se Comprueba si la conexión se estableció correctamente
if conexion.is_connected():
    print("Conexión exitosa a la base de datos")
else:
    print("Error al conectar a la base de datos")

#Puntero
cursor = conexion.cursor()


consulta = "SELECT * FROM Jugadores1"
cursor.execute(consulta)


resultados = cursor.fetchall()

for fila in resultados:
    print(fila)


cursor.close()
conexion.close()
