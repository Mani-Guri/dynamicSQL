import mysql.connector as c
def finder(host, user, password, database, table_name):
    try:
        mydb = c.connect(host=host, user=user, password=password, database=database)  
        cursor = mydb.cursor()
        cursor.execute(f"DESC {table_name}")
        columns = cursor.fetchall()
        print("Columns in the table:")
        for column in columns:
            print(column[0])
        selected_column = input("Select a column from the above list:\n>> ")
        if selected_column in [column[0] for column in columns]:
            return selected_column
        else:
            print("Invalid column name.")
            return None
          
    except c.Error as e:
        print(f"Error: {e}")
        return None
    
    finally:
        if mydb and mydb.is_connected():
            mydb.close()