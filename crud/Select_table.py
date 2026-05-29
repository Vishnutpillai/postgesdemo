import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from db import get_db_connection

def select_tables(id):
    conn = get_db_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            insert_table_query='''
            SELECT * FROM users WHERE id=%s;
            '''
            cursor.execute(insert_table_query, (id,))
            user=cursor.fetchone()
            cursor.close()
            if user:
                print(f'user found: {user}')
            else:
                print(f'user with id {id} not found')
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            conn.close()
# select_tables(1001)