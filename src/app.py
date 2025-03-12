from flask import Flask, jsonify
import mysql.connector
import os

app = Flask(__name__)

# Configuración de conexión a MySQL
db_config = {
    "host": os.getenv("MYSQL_HOST", "localhost"),
    "user": os.getenv("MYSQL_USER", "root"),
    "password": os.getenv("MYSQL_PASSWORD", "rootpassword"),
    "database": os.getenv("MYSQL_DATABASE", "mydatabase"),
}

def connect_db():
    return mysql.connector.connect(**db_config)

@app.route("/")
def hello_world():
    return "¡Hola Mundo desde la República Dominicana! | ITLA | Emmanuel Soto 2022-2092"

@app.route("/data")
def get_data():
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT NOW() as time")
        result = cursor.fetchone()
        conn.close()
        return jsonify({"message": "Datos desde MySQL", "time": result[0]})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
