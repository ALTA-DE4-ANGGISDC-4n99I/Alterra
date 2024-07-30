import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.types import BigInteger, String, DateTime
from sqlalchemy.exc import SQLAlchemyError

class DatabaseHandler:
    def __init__(self):
        self.engine = None
        self.db_name = None

    def __create_connection(self):
        user = "postgres"
        password = "anggi1723"
        host = "localhost"
        database = "postgres"
        port = 5432
        conn_string = f"postgresql://{user}:{password}@{host}:{port}/{database}"
        self.engine = create_engine(conn_string)

    def to_postgres(self, db_name: str, data: pd.DataFrame):
        self.db_name = db_name
        self.__create_connection()

        try:
            df_schema = {
                "VendorID": BigInteger,
                "tpep_pickup_datetime": DateTime,
                "tpep_dropoff_datetime": DateTime,
                "passenger_count": BigInteger,
                "trip_distance": BigInteger,
                "RatecodeID": BigInteger,
                "store_and_fwd_flag": String(1),
                "PULocationID": BigInteger,
                "DOLocationID": BigInteger,
                "payment_type": BigInteger,
                "fare_amount": BigInteger,
                "extra": BigInteger,
                "mta_tax": BigInteger,
                "tip_amount": BigInteger,
                "tolls_amount": BigInteger,
                "improvement_surcharge": BigInteger,
                "total_amount": BigInteger,
                "congestion_surcharge": BigInteger
            }
            data.to_sql(
                name=self.db_name, 
                con=self.engine, 
                if_exists="replace", 
                index=False, 
                schema="public", 
                dtype=df_schema, 
                method=None, 
                chunksize=5000
            )
        except SQLAlchemyError as err:
            print("error >> ", err.__cause__)


csv_file = '.\ingestion-data\dataset\sample.csv'
df = pd.read_csv(csv_file)

handler = DatabaseHandler()
handler.to_postgres("ingestion", df)
