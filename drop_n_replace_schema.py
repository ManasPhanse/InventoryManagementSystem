import mysql.connector
from getpass import getpass

# Connect to MySQL database
def create_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password=getpass("Enter Password: "),
        database="inventory"
    )

conn = create_connection()
cursor = conn.cursor()

# Drop the schema
cursor.execute('DROP SCHEMA IF EXISTS inventory')
print('Dropped Schema')

# Create a new schema 
cursor.execute('CREATE SCHEMA IF NOT EXISTS inventory')
print('New Schema Created')

# Commit the changes
conn.commit()

# Close the connection
cursor.close()
conn.close()
