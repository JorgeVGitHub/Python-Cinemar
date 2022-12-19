import sqlite3 as alfa

def crear_db():
    conexion = alfa.connect("cinemar.db")
    consulta = """CREATE TABLE IF NOT EXISTS Usuario(
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        nombre TEXT)"""
    cursor = conexion.cursor()
    cursor.execute(consulta)
    conexion.commit()
    conexion.close()

def insertar_usuario(nombre):
    conexion = alfa.connect ("cinemar.db")
    consulta = f"INSERT INTO Usuario VALUES(NULL,'{nombre}')"
    cursor = conexion.cursor()
    cursor.execute(consulta)
    conexion.commit()
    conexion.close()

 