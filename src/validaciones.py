from flask import Flask, request, jsonify #importar librerias
from flask_mysqldb import MySQL #configuracion de la base de datos
from app import mysql
from config import config
#validamos para ver si la cedula qeu ingreso el usuario ya existe en la base de datos
def validar_cedula(cedula):
    try:#el try es para que si hay un error no se caiga el programa
        cursor = mysql.connection.cursor()#se usa para conectar con la base de datos
        cursor.execute('select Cedula from heroku_978ea61906c2949.usuario where Cedula = {0}'.format(cedula))#se usa para mostrar los datos de la tabla usuario
        datos = cursor.fetchall()#el fetchall es para que se muestren todos los datos de la consulta
        if len(datos) > 0:#se crea un ciclo for para que se muestren todos los datos de la consulta
            return True
        else:
            return False
    except Exception as e:#el except es para que si hay un error no se caiga el programa
        return jsonify({'message': 'error'})#en caso de que haya un error se retorna un mensaje de error