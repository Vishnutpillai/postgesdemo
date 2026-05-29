import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from db import get_db_connection

def update_table(id, new_name):
    conn = get_db_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            Update_table_query = '''
            UPDATE users SET name=%s WHERE id=%s;
            '''
            cursor.execute(Update_table_query,(new_name,id))
            conn.commit()
            print(f"user with id {id} updated successfully")
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            cursor.close()
            conn.close()
update_table(1001,'Vishnu T Pillai')
