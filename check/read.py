import mysql.connector as c,check
def run(op,host,user,password,database):
    mydb = c.connect(host=host,user=user,password=password,database=database)
    print(f'Your Database is [{database}]')
    cursor = mydb.cursor()
    if op=='1':
        select = "show tables;"
        cursor.execute(select)
        result = cursor.fetchall()
        for i in result.__iter__():
            print("Table name",i[0])
        mydb.commit()
    elif op=='2':
        table_name = check.check_database_empty(host,user,password,database)
        select = f"desc {table_name};"
        cursor.execute(select)
        result=cursor.fetchall()
        for i in result.__iter__():
            print(f"column name = {i[0]} | datatype ={i[1]}")
        mydb.commit()
    elif op=='3':
        table_name = check.check_database_empty(host,user,password,database)
        select = f"select * from {table_name};"
        cursor.execute(select)
        show_database = cursor.fetchall()
        for i in show_database.__iter__():
            print(i)
    elif op=='4':
        table_name = check.check_database_empty(host,user,password,database)
        col_name = input("Enter column name = ")
        try:
            select = f"select {col_name} from {table_name};"
            cursor.execute(select)
            result = cursor.fetchall()
            print(f"column '{col_name}'")
            num = 1
            for i in result.__iter__():
                print(f"{num}.",i[0])
                num+=1
        except Exception:
            print(f"Their is no column named {col_name}")
    else:
        print("Please enter valid operation!!!")
    print('_'*80)