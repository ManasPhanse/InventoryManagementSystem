import mysql.connector
from getpass import getpass

def create_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password=getpass("Enter Password: "),
        database="inventory"
    )

def execute_sql_file(cursor, file_path):
    with open(file_path, 'r') as sql_file:
        sql_commands = sql_file.read()
        
        # Split the commands by semicolon and execute them one by one
        for command in sql_commands.split(';'):
            if command.strip():
                cursor.execute(command)

def main():
    conn = create_connection()
    cursor = conn.cursor()
    
    # Path to your .sql file
    sql1 = 'master_tables.sql'
    sql2 = 'transaction_tables.sql'
    
    try:
        execute_sql_file(cursor, sql1)
        execute_sql_file(cursor, sql2)
        conn.commit()
        print("SQL files executed successfully.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    main()
