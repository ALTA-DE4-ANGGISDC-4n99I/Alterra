from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError

def create_connection():
    user = "postgres"
    password = "anggi1723"
    host = "localhost"
    database = "postgres"
    port = 5432
    conn_string = f"postgresql://{user}:{password}@{host}:{port}/{database}"
    
    try:
        engine = create_engine(conn_string)
        connection = engine.connect()
        connection.close()
        print("Koneksi berhasil!")
        return engine
    except SQLAlchemyError as err:
        print("Koneksi gagal: ", err.__cause__)
        return None

engine = create_connection()
