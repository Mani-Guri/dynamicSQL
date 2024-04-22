import mysql.connector as c,check
def run(op,host,user,password,database):
    mydb = c.connect(host=host,user=user,password=password,database=database)
    cursor = mydb.cursor()   
    table_name = check.check_database_empty(host,user,password,database)
    if op==1:
        sno = int(input("Enter serial number = "))
        if check.checker.result(sno)==True:
            dele = f"delete from {table_name} where sno={sno}"
            cursor.execute(dele)
            mydb.commit()
            print("DELETED!!!!!")
        else:
                print(f"This Serial number is not in database")
    elif op==2:
        col_name = input("Enter column name you want to delete = ")
        try:
            dele = f"alter table {table_name} drop column {col_name};"
            cursor.execute(dele)
            mydb.commit()
        except Exception:
            print(f"Their is no column named {col_name}") 
    else:
        print(f"Your Database is [{database}] and table [{table_name}]")
        confirm = input(f"You Really want to delete your table {table_name}?\n->Press 'YES'")
        if confirm.lower() == 'yes':
            dele=f"drop table {table_name};"
            cursor.execute(dele)
            mydb.commit()
            print(f"TABLE {table_name} IS BEEN DELETED!!")
        else:
            print("Only 'YES' is accepted as CONFIRMATION!")


