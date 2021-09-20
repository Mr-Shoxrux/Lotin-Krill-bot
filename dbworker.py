import sqlite3
import pandas as pd
import numpy as np
class DBHelper:
     def __init__(self,db_name):
         try:
             self.conn=sqlite3.connect(db_name,check_same_thread=False)
             self.conn.row_factory=sqlite3.Row
             self.cursor=self.conn.cursor()
             self.cursor.execute('''CREATE TABLE Data
                 ([generated_id] INTEGER PRIMARY KEY,[user_id] integer, [state] integer)''')
             print("creted")
         except Exception as ex:
             pass

     def set_state(self,user_id,state):
         try:
             df = pd.read_sql_query('SELECT * FROM Data;', self.conn)
             users = np.array(df['user_id'])
             if user_id in users:
                 sql_update_query = "Update Data set state = "+str(state)+"  where user_id = "+str(user_id)
                 self.cursor.execute(sql_update_query)
                 self.conn.commit()
             else:
                 sqlite_insert_with_param = """INSERT INTO Data
                                       (user_id, state) 
                                       VALUES (?, ?);"""

                 data_tuple = (user_id,state)
                 self.cursor.execute(sqlite_insert_with_param, data_tuple)
                 self.conn.commit()
         except Exception as ex:
             pass


     def get_state(self,user_id):
         try:
             df = pd.read_sql_query('SELECT * FROM Data;', self.conn)
             users = np.array(df['user_id'])
             states = np.array(df['state'])
             dictionary=dict(zip(users, states))

             return dictionary[user_id]
         except Exception as ex:
             pass
