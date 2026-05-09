"""datasource.py

Code using the psycopg2 Python library to 
connect to a database and execute two queries.
"""

import psycopg2 as ps
import psqlConfig as config

def connect():
    """Establishes a connection to the database with the following credentials:
        user - username, which is also the name of the database
        password - the password for this database on perlman

    Returns: a database connection.

    Note: exits if a connection cannot be established.
    """
    try:
        connection = ps.connect(database=config.database, user=config.user, password=config.password, host="localhost")
    except Exception as e:
        print("Connection error: ", e)
        exit()
    return connection

def get_row(connection, llm_name: str) -> list:
    """Retrieves all data in a given LLMs row.

    Args:
        connection (psycopg2.connection) - the connection to the database
        llm_name (str) - llm model name from column one 

    Returns:
        list - a list of the values in the row, or None if the query fails. 
    """
    try:
        cursor = connection.cursor()
        query = "SELECT * FROM llm_energy WHERE model_name = '" + llm_name + "';"
        cursor.execute(query, (llm_name,))
        return cursor.fetchall()

    except Exception as e:
        print ("Something went wrong when executing the query: ", e)
        return None

def get_column(connection, column_name: str) -> list:
    """Retrieves all data in a given column.

    Args:
        connection (psycopg2.connection) - the connection to the database
        column_name (str) - a specified column label 

    Returns:
        list - a list of the values in the column, or None if the query fails. 
    """
    try:
        cursor = connection.cursor()
        query = "SELECT " + column_name + " FROM llm_energy;"
        cursor.execute(query, (column_name,))
        return cursor.fetchall()

    except Exception as e:
        print ("Something went wrong when executing the query: ", e)
        return None

def main():
    # Connect to the database
    connection = connect()

    # Executes query one 
    results = get_row(connection, "BLOOM")
    
    if results is not None:
        print("Query results: ")
        for item in results:
            print(item)

    # Executes query two 
    results = get_column(connection, "model_name")
    
    if results is not None:
        print("Query results: ")
        for item in results:
            print(item)

    # Disconnect from database
    connection.close()

main()