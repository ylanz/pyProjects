from dbMS import DataBase
import json
#import jsonify

mydb = DataBase("localhost", "root", "","test")

mydb.conectarDB()


#data = mydb.leerDatos("SELECT * FROM tb_tareas WHERE nombre LIKE '%(name)s'", {'name':"s"})
#data = mydb.leerDatos("SELECT * FROM tb_tareas WHERE nombre = %s", ("tarea 1", ))
#data = mydb.leerDatos("SELECT * FROM tb_tareas WHERE nombre LIKE %s", "%s")
#for row in data:
 #   print(row)

mydb.inmodDatos("INSERT INTO tb_tareas (nombre, descripcion) VALUES (%s, %s)", ("22222", "testing"))
cur = mydb.getCursor()
print("Last insert: ", cur.lastrowid)
#row_headers=[x[0] for x in cur.description]
#json_data=[]
#for result in data:
#    json_data.append(dict(zip(row_headers, result)))

#print(json.dumps(json_data))
#data = mydb.leerDatos("SELECT * FROM tb_tareas WHERE nombre LIKE %s", "%s")
#print(data)
#print(json.dumps(data))

mydb.cerrarCnn()