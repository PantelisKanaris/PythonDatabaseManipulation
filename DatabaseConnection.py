"""
Connects to a SQL database using pyodbc
"""
import pyodbc
import os
from dotenv import load_dotenv
    
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
db_serverName = os.getenv("DB_SERVER")
db_databaseName = os.getenv("DB_DATABASE")
db_connection = os.getenv("DB_CONNECTION")
db_driver = os.getenv("DB_DRIVER")

connection = pyodbc.connect(f'DRIVER={db_driver};'
                            f'SERVER={db_serverName};'
                            f'DATABASE={db_databaseName};'
                            f'{db_connection}'
                            )

cursor = connection.cursor()
cursor.execute("SELECT * FROM Persons")
for row in cursor.fetchall():
    print(row)