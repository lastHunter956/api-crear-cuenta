class DevelopmentConfig():
    DEBUG = True
    MYSQL_HOST = 'us-cdbr-east-06.cleardb.net'#configuracion de la base de datos host
    MYSQL_USER = 'bbd292aa23aeaf'#configuracion de la base de datos usuario
    MYSQL_PASSWORD = 'ece55924'#configuracion de la base de datos contraseña
    MYSQL_DB = 'heroku_978ea61906c2949'#configuracion de la base de datos


config = {
    'development': DevelopmentConfig
}
