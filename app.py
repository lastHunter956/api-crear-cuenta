from flask import Flask, request, jsonify #importar librerias
from flask_mysqldb import MySQL #configuracion de la base de datos
from requests import post #configuracion de la base de datos
from werkzeug.security import generate_password_hash, check_password_hash
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
app.config['MYSQL_HOST'] = 'us-cdbr-east-06.cleardb.net'#configuracion de la base de datos host
app.config['MYSQL_USER'] = 'bbd292aa23aeaf'#configuracion de la base de datos usuario
app.config['MYSQL_PASSWORD'] = 'ece55924'#configuracion de la base de datos contraseña
app.config['MySQL_DB'] = 'heroku_978ea61906c2949'#configuracion de la base de datos

mysql = MySQL(app) #se usa para mostrar los datos de la tabla vehiculo

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
def validar_correo(correo):
    try:#el try es para que si hay un error no se caiga el programa
        cursor = mysql.connection.cursor()#se usa para conectar con la base de datos
        cursor.execute('select Correo from heroku_978ea61906c2949.usuario where Correo = {0}'.format(correo))#se usa para mostrar los datos de la tabla usuario
        datos = cursor.fetchall()#el fetchall es para que se muestren todos los datos de la consulta
        if len(datos) > 0:#se crea un ciclo for para que se muestren todos los datos de la consulta
            return True
        else:
            return False
    except Exception as e:#el except es para que si hay un error no se caiga el programa
        return jsonify({'message': 'error'})#en caso de que haya un error se retorna un mensaje de error
@app.route('/')#ruta de la pagina inicial
def hello_world():#funcion de la pagina inicial
    return 'Hello, World!'

#mostrar los datos de la tabla personas
@app.route('/signup', methods=['GET'])
def get_usuario():
    try:#el try es para que si hay un error no se caiga el programa
        cursor = mysql.connection.cursor()#se usa para conectar con la base de datos
        cursor.execute('select Cedula, Nombre, Apellido, Correo from heroku_978ea61906c2949.usuario')#se usa para mostrar los datos de la tabla usuario
        datos = cursor.fetchall()#el fetchall es para que se muestren todos los datos de la consulta
        personas = []#se crea una lista vacia donde se guardaran los datos de los vehiculos
        for fila in datos:#se crea un ciclo for para que se muestren todos los datos de la consulta
            dato = {'Cedula': fila[0], 'Nombre y apellido': fila[1]+" "+ fila[2], 'Correo': fila[3]}#se crea un diccionario para que se muestren los datos de los usuarios
            personas.append(dato)#se agrega los datos de los usuarios a la lista
        return jsonify({'personas': personas, 'message': 'ok'})
    except Exception as e:#el except es para que si hay un error no se caiga el programa
        return jsonify({'message': 'error'})#en caso de que haya un error se retorna un mensaje de error
#registrar una persona
@app.route('/signup', methods=['POST'])
def post_usuario():
    try:# el try es para que si hay un error no se caiga el programa
        cursor = mysql.connection.cursor()#se usa para conectar con la base de datos
        cedula = request.json['Cedula']#se usa para obtener los datos de la cedula
        correo = request.json['Correo']#se usa para obtener los datos del correo
        contraseña = request.json['Contraseña']#se usa para obtener los datos de la contraseña
        if validar_cedula(cedula) and validar_correo(correo):#se usa para validar si la cedula ya existe en la base de datos
            return jsonify({'message': 'la cuenta o la cedula ya fue registrada'})#error
        else:
            sql = """INSERT INTO heroku_978ea61906c2949.usuario(Correo,Cedula, Direccion, Nombre, Apellido, Ciudad, Pais, Contraseña) 
            VALUES ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}')""".format(correo,cedula, request.json['Direccion'], request.json['Nombre'], request.json['Apellido'], request.json['Ciudad'], request.json['Pais'], generate_password_hash(contraseña),correo)#se usa para insertar datos en la tabla usuario''])
            cursor.execute(sql)#se ejecuta la consulta
            mysql.connection.commit()#guardar los cambios
            return jsonify({'message': 'persona añadida'})#se retorna un mensaje de vehiculo añadido

    except Exception as e:#el except es para que si hay un error no se caiga el programa
        return jsonify({'message': 'error'})#en caso de que haya un error se retorna un mensaje de error   

@app.route('/signup/<cedula>', methods=['PUT'])
def put_usuario(cedula):
    try:#el try es para que si hay un error no se caiga el programa
        cursor = mysql.connection.cursor()#se usa para conectar con la base de datos
        sql = """UPDATE heroku_978ea61906c2949.usuario SET Correo='{0}', Direccion='{1}', Nombre='{2}', Apellido='{3}', Ciudad='{4}', Pais='{5}' WHERE Cedula='{6}'""".format(request.json['Correo'], request.json['Direccion'], request.json['Nombre'], request.json['Apellido'], request.json['Ciudad'], request.json['Pais'], cedula)#se usa para actualizar los datos de la tabla usuario
        cursor.execute(sql)#se ejecuta la consulta
        mysql.connection.commit()#guardar los cambios
        return jsonify({'message': 'persona actualizada'})#se retorna un mensaje de persona actualizada
    except Exception as e:
        return jsonify({'message': 'error'})#en caso de que haya un error se retorna un mensaje de error

def pagina_no_encontrada(error):
    return "<h1>Página no encontrada</h1>", 404


if __name__== "__main__" :
    app.run(debug=True, port=5000)
