from dotenv import load_dotenv
import os

# Load .env.local
load_dotenv('.env.local')

import mysql.connector
from mysql.connector import errorcode

try:
    # Connect to MySQL server
    connection = mysql.connector.connect(
        host="localhost",       # change if your server is different
        user="root",            # change to your MySQL username
        password= os.getenv("DB_PASSWORD") # change to your MySQL password
    )

    cursor = connection.cursor()

    # Create database if it doesn't exist
    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

    print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # Close cursor and connection
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
