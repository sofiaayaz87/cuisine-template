import mysql.connector
import os

DB_HOST = os.environ.get("MYSQL_HOST", "localhost")
DB_PORT = int(os.environ.get("MYSQL_PORT") or 3306)
DB_USER = os.environ.get("MYSQL_USER", "root")
DB_PASS = os.environ.get("MYSQL_PASSWORD", "")
DB_NAME = os.environ.get("MYSQL_DATABASE", "smart_restaurant_finder")

try:
    db = mysql.connector.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASS,
        database=DB_NAME,
        auth_plugin='mysql_native_password'
    )

    cursor = db.cursor(buffered=True)
    cursor.execute("SHOW TABLES;")
    _ = cursor.fetchall()

    print("Database connected successfully!")

except mysql.connector.Error as err:
    print("Connection error:", err)
    db = None
    cursor = None
