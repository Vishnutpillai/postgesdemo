import psycopg2
from psycopg2 import sql,OperationalError
import psycopg2.extras

import os
from dotenv import load_dotenv
load_dotenv()
conn=None
#Function to connect to the Database
def get_db_connection():
    try:
        conn=psycopg2.connect(
            host=os.getenv('HOST'),
            database=os.getenv('DATABASE'),
            user=os.getenv('USER'),
            password=os.getenv('PASSWORD'),
            port=os.getenv('PORT')
        )
        print('Connection to postgreSQL DB successful')
        return conn
    except OperationalError as e:
        print(f"The error '{e}' occured")
        return None
    
# connection=get_db_connection()