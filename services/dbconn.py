from dotenv import load_dotenv
import os, psycopg2

load_dotenv()

def db_connection():
    conn = psycopg2.connect(
        host = os.getenv("HOST"),
        dbname = os.getenv("DBNAME"),
        user = os.getenv("USER"),
        password = os.getenv("PASSWD"),
        port = os.getenv("PORT")
    )
    return conn