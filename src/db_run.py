import sqlite3
import pandas as pd

class DatabaseExecutor:
    def __init__(self, db_path):
        self.db_path = db_path

    def db_execute_query(self, sql_query):
        # Connect to SQLite database (or create one if it doesn't exist)
        conn = sqlite3.connect(self.db_path)
        
        # Create a cursor object
        cursor = conn.cursor()
        
        # Execute SQL query
        cursor.execute(sql_query)
        
        # Fetch results
        results = cursor.fetchall()
        
        # Create DataFrame from results
        df = pd.DataFrame(results, columns=[desc[0] for desc in cursor.description])
        
        # Close the connection
        conn.close()
        
        return df