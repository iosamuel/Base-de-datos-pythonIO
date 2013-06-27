#import MySQLdb as mdb
import sqlite3

coneccion = sqlite3.connect('pythonio.db')
coneccion.row_factory = sqlite3.Row
# coneccion = mdb.connect(user="root", passwd="samuel1996", db="pythonio")
# coneccion.cursorclass = mdb.cursors.DictCursor

cursor = coneccion.cursor()

try:
	cursor.execute('CREATE TABLE productos (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre VARCHAR(45), descripcion TEXT, precio INT)')
except:
	pass

productos = [
	('Manzana', 'Verde', 2),
	('Naranja', 'anaranjada', 4),
	('Limon', 'Verde', 3)
]
cursor.executemany('INSERT INTO productos VALUES (NULL, ?, ?, ?)', productos)
#cursor.executemany('INSERT INTO productos VALUES (NULL, %s, %s, %s)', productos)
#cursor.execute('INSERT INTO productos VALUES (NULL, %s, %s, %s)', ('Manzana', 'Verde', 2))
coneccion.commit()
#coneccion.rollback()

cursor.execute('SELECT * FROM productos')

#cursor.fetchone()
#cursor.fetchmany(n)
resultados = cursor.fetchall()
for res in resultados:
	print res['id']
	print res['nombre']

cursor.close()
coneccion.close()