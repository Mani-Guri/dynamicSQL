import mysql.connector as c,check,crud
def cr_db(host,user,password,database):
    mydb = c.connect(host=host,user=user,password=password)
    cursor = mydb.cursor()
    create = f"create database {database};"
    cursor.execute(create)
    mydb.commit()
    use = f"use {database};"
    cursor.execute(use)
    mydb.commit()
    print("-"*80)
    print(f"Database Created [{database}]")
    option = input("Want To Make Table? YES:NO\n>>")
    if option.lower() == 'yes':
        r_table_name = Table_make(host,user,password,database)
        want = input("Want to insert Data? YES:NO\n>>")
        if want.lower() =='yes':
            insert_data(r_table_name,host,user,password,database)
        else:
              print("Data Insertion Skipped!!")
    else:
        print("Creating Table Skipped!!")
def Table_make(host,user,password,database):
    mydb = c.connect(host=host,user=user,password=password,database=database)
    cursor = mydb.cursor()
    table_name = input("Enter Table Name = ")
    print("-"*80)
    print(f"You are in Table [{table_name}]")
    col_num = int(input("How Many Columns You Want?\n>>"))
    lst = []
    for i in range(1,col_num+1):
        col_name = input(f"Enter Column:{i} Name = ")
        datatype = input("Enter the datatype = ")
        lst.append(f"{col_name} {datatype}")
    tup = tuple(lst)
    res = ', '.join(tup)
    create = f"create table {table_name} ({res});"
    cursor.execute(create)
    mydb.commit()
    return table_name
def insert_data(r_table_name,host,user,password,database):
    mydb = c.connect(host=host,user=user,password=password,database=database)
    cursor = mydb.cursor()
    data = f"desc {r_table_name};"
    cursor.execute(data)
    val = cursor.fetchall()
    num = int(input(f"How Many Values You Want To Insert into [{r_table_name}]?\n>>"))
    for i in range(num):
        row_values = []
        for column in val:
            in_val = input(f"Enter value of [{column[0]}]-[{column[1]}]:{i+1} = ")
            row_values.append(in_val)
        row_values_str = ', '.join(row_values)
        insert_query = f"INSERT INTO {r_table_name} VALUES ({row_values_str});"
        cursor.execute(insert_query)
        mydb.commit()
        print("-"*40)
    print("Data inserted successfully.")

def existed_database(host,user,password,database):
    mydb = c.connect(host=host,user=user,password=password)
    cursor = mydb.cursor()
    use = f"use {database};"
    cursor.execute(use)
    mydb.commit()
    display = f"[Database {database}]"
    print(f"{display:-^70}")
    r_check_table = check.check_database_empty(host,user,password,database)
    if r_check_table == True:
        option = input("Want To Make Table? YES:NO\n>>")
        if option.lower() == 'yes':
            r_table_name = Table_make(host,user,password,database)
            want = input("Want to insert Data? YES:NO\n>>")
            if want.lower() =='yes':
                insert_data(r_table_name,host,user,password,database)
            else:
                print("Data Insertion Skipped!!")
        else:
            print("Creating Table Skipped!!")
    else:
        try:
            option = r_check_table
            want = input("Want to insert Data? YES:NO\n>>")
            if want.lower() =='yes':
                insert_data(option,host,user,password,database)
            else:
                print("Data Insertion Skipped!!")
        except Exception:
            print(f"This table is not present in [{database}]")
