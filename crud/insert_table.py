import os 
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from db import get_db_connection

def insert_table(id,name):
    conn=get_db_connection()
    if conn is not None:
        try:
            cursor=conn.cursor()
            insert_value_table='''
            INSERT INTO users(id, name) VALUES(%s,%s);
            '''
            cursor.execute(insert_value_table,(id,name))
            conn.commit()
            print(f"user {name} created successfully")
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            cursor.close()
            conn.close()
# insert_table(1001,'Vishnu')
insert_table(1002,'Rahul R')