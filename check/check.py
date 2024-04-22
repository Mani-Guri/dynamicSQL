import mysql.connector as c

def connect_to_database1(host, user, password, database):
    try:
        mydb = c.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        print(f"Connected to the database [{database}] successfully!")
        mydb.close()
        return True
    except c.Error as err:
        if err.errno == 1045: 
            print("Access denied. Check your username or password.")
        elif err.errno == 1049:  
            print("Unknown database. Check the database name.")
        elif err.errno == 2005:  
            print("Unknown host. Check the host address.")
        else:
            print(f"Error: {err}")
        return False
def connect_to_database2(host,user,password):
    try:
        mydb = c.connect(
            host = host,
            user = user,
            password = password
        )
        print("Connected Successfully!")
        mydb.close()
        return True
    except c.Error as err:
        if err.errno == 1045:
            print("Access denied. Check your username or password.")
        elif err.errno == 2005:
            print("Unknown host. Check the host address.")
        else:
            print(f"Error: {err}")
        return False

def check_database_empty(host, user, password, database):
    mydb = c.connect(host=host,user=user,password=password,database=database)
    cursor = mydb.cursor()
    cursor.execute("SHOW TABLES")
    tables = cursor.fetchall()
    if not tables:
        print("Database is empty.")
        return True
    else:
        print("Database contains tables.")
        for i in tables:
            print(f"{i[0]}")
        option = input("Which table you want to use = ")
        flag = 0
        for i in tables:
            if option == i[0]:
                flag = 1
        if flag == 1:
            return option
        else:
            print(f"Their is no table [{option}] in database [{database}]")
            want = input("Want to Re-try?? YES:NO\n>>")
            if want.lower() == 'yes':
                check_database_empty(host, user, password, database)
            else:
                print("Exited!!!")
# later added
def checker(host,user,password,database):
    mydb = c.connect(host=host,user=user,password=password,database=database)
    if mydb.is_connected():
        def result(sno)->None:
            cursor = mydb.cursor()
            table_name = check_database_empty(host,user,password,database)
            select = f"select * from {table_name};"
            cursor.execute(select)
            data = cursor.fetchall()
            for row in data:
                if row[1]==sno:
                    return True