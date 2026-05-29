import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from db import get_db_connection

def delete_table():
    conn=get_db_connection()
    if conn is not None:
        try:
            cursor=conn.cursor()
            delete_table_query='''
            DROP TABLE IF EXISTS users;
            '''
            cursor.execute(delete_table_query)
            conn.commit()
            print("Table 'users' deleted successfully." )
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            cursor.close()
            conn.close()
# delete_table()