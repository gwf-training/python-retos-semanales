### Reto #23: LA BASE DE DATOS
#### Publicación: 06/06/23 | MEDIA

# Realiza una conexión desde el lenguaje que hayas seleccionado a la siguiente
# base de datos MySQL:
# - Host: mysql-5707.dinaserver.com
# - Port: 3306
# - User: mouredev_read
# - Password: mouredev_pass
# - Database: moure_test
# 
# Una vez realices la conexión, lanza la siguiente consulta e imprime el resultado:
# - SELECT * FROM `challenges`
# 
# Se pueden usar librerías para realizar la lógica de conexión a la base de datos.

#python -m pip install mysql-connector-python
import mysql.connector

config = {
    "host": "mysql-5707.dinaserver.com",
    "port": "3306",
    "database": "moure_test",
    "user": "mouredev_read",
    "password": "mouredev_pass" 
}

def get_challenges():
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()

    query = "SELECT * FROM challenges"
    cursor.execute(query)
    result = cursor.fetchall()

    cursor.close()
    connection.close()
    return result


if __name__ == '__main__':
    print('Reto #23: LA BASE DE DATOS')
    print('Publicación: 06/06/23 | MEDIA')
    result = get_challenges()
    for row in result:
        print(row)
