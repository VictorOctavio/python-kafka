import json

# PostgreSQL
from psycopg2 import sql
import psycopg2

# Kafka
from kafka import KafkaProducer

# Configuración de la conexión a la base de datos
connection_config = {
    'dbname': 'postgres',
    'user': 'postgres',
    'password': 'postgres',
    'host': 'localhost',
    'port': 5433
}

# Función para conectar a la base de datos
def connect():
    try:
        connection = psycopg2.connect(**connection_config)
        return connection
    except psycopg2.Error as e:
        print("Error al conectar a la base de datos:", e)
        return None

# Función para crear un nuevo usuario
def create_user(nombre, email):
    connection = connect()
    if connection:
        try:
            with connection.cursor() as cursor:
                query = sql.SQL("INSERT INTO {} ({}, {}) VALUES (%s, %s) RETURNING id, nombre, email").format(
                    sql.Identifier('users'),
                    sql.Identifier('nombre'),
                    sql.Identifier('email')
                )
                cursor.execute(query, (nombre, email))
                user = cursor.fetchone()
                connection.commit()
                send_user_to_kafka(user) # send kafka
        except psycopg2.Error as e:
            print("Error al insertar el usuario:", e)
        finally:
            connection.close()

def send_user_to_kafka(user):
    producer = KafkaProducer(
        bootstrap_servers="localhost:9092",
        value_serializer=lambda v: json.dumps(v).encode("utf-8")
    )
    # Enviar información del usuario al topic 'auth'
    producer.send("auth", {"id": user[0], "nombre": user[1], "email": user[2]})
    producer.flush()

# Función para obtener todos los usuarios
def get_all_users():
    connection = connect()
    if connection:
        try:
            with connection.cursor() as cursor:
                query = sql.SQL("SELECT * FROM {}").format(sql.Identifier('users'))
                cursor.execute(query)
                users = cursor.fetchall()
                print("Usuarios:")
                for user in users:
                    print(user)
        except psycopg2.Error as e:
            print("Error al obtener los usuarios:", e)
        finally:
            connection.close()
            