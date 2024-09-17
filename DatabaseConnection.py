"""
Connects to a SQL database using pyodbc
"""
import pyodbc
import os
from dotenv import load_dotenv
from contextlib import contextmanager
    
# This is a temporary solution it 
# Set the working directory to the script's directory
# script_dir = os.path.dirname(os.path.realpath(__file__))
# os.chdir(script_dir)

# # Load environment variables from .env file
# load_dotenv('Variables.env')


# Get environment variables
# db_serverName = os.getenv('DB_SERVER')
# db_databaseName = os.getenv('DB_DATABASE')
# db_connection = os.getenv('DB_CONNECTION')
# db_driver = os.getenv('DB_DRIVER')

# Access the variables

# This function is use to connect to the database and it returns the cursor 
def connectToDatabase():

    db_serverName = os.getenv("DB_SERVER")
    db_databaseName = os.getenv("DB_DATABASE")
    db_connection = os.getenv("DB_CONNECTION")
    db_driver = os.getenv("DB_DRIVER")

    connection = pyodbc.connect(f'DRIVER={db_driver};'
                                f'SERVER={db_serverName};'
                                f'DATABASE={db_databaseName};'
                                f'{db_connection};'
                                'Pooling=True;'
                                )
     # Return the connection
    return connection

@contextmanager
def GetDatabaseConnection():
    connection = connectToDatabase()
    try:
        yield connection
    finally:
        connection.close()

def fetch_data_from_db(query):
    with GetDatabaseConnection() as conn:
        cursor = conn.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    
   # creates the tables this function will be used  to create the database shema? Most likely we will do it manually. 
def CreateDatabase():
    # SQL query to create the Users table this is tempory will create a library for automatic querry creation
    createTables = '''
  CREATE TABLE Users (
  UserID INT PRIMARY KEY IDENTITY(1,1),  
  Username VARCHAR(255) NOT NULL,        
  Email VARCHAR(255) NOT NULL UNIQUE,    
  Password VARCHAR(255) NOT NULL        
  );
   '''      
    with GetDatabaseConnection() as db: # here i manage the connection
        cursor = db.cursor()
        cursor.execute(createTables)  # Execute the CREATE TABLE query
        db.commit()  # Commit the transaction to apply the table creation
    
    
