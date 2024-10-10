import cx_Oracle

# Conexión a la base de datos
connection = cx_Oracle.connect("usuario/contraseña@nombre_del_servidor:puerto/nombre_de_la_base_de_datos")
cursor = connection.cursor()

cursor.execute("SELECT * FROM tabla")
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.close()
connection.close()
