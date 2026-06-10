import os
import psycopg2
from flask import Flask, render_template, request

app = Flask(__name__)

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "credenciales")
DB_USER = os.getenv("DB_USER", "admin")
DB_PASSWORD = os.getenv("DB_PASSWORD", "admin123")


def conectar_db():
    return psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )


@app.route("/", methods=["GET", "POST"])
def login():
    usuario_encontrado = None
    error = None

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        try:
            conn = conectar_db()

            with conn.cursor() as cursor:
                cursor.execute("""
                    SELECT u.id_usuario, u.nombre, u.correo, u.telefono, u.fecha_nacimiento
                    FROM credenciales c
                    JOIN usuarios u ON c.id_usuario = u.id_usuario
                    WHERE c.username = %s AND c.password_hash = %s;
                """, (username, password))

                usuario_encontrado = cursor.fetchone()

                if not usuario_encontrado:
                    error = "Usuario o contraseña incorrectos."

        except Exception as e:
            error = f"Error de conexión o consulta: {e}"

        finally:
            if 'conn' in locals():
                conn.close()

    return render_template(
        "login.html",
        usuario=usuario_encontrado,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")