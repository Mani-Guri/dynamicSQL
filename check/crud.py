import mysql.connector as c,new_db,updating as us,read,deletion,check
def db_run(host,user,password,database):
    mydb = c.connect(host=host,user=user,password=password,database=database)
    if mydb.is_connected():
        print(f'Your Database is [{database}]')
        con = input("WELCOME....TO OPREATE 'CRUD' OPERATION PRESS 'yes'/'YES'/'y'/'Y' \n>>")
        while con.lower() == 'yes' or con.lower()=='y':
            cursor = mydb.cursor()
            table_name = check.check_database_empty(host,user,password,database)
            for num in range(1):
                select = f"select * from {table_name}"
                cursor.execute(select)
                show_database = cursor.fetchall()
                print(f'Your Table is [{table_name}]')
                for i in show_database.__iter__():
                    print(i)
                print('_'*80)
            operation = input("What you want to do in MySql:\n-->1.CREATE\n-->2.READ\n-->3.UPDATE\n-->4.DELETE\n>>")
            if operation=='1':
                print(f"Inserting new records or rows into database [{database}] table [{table_name}]")
                new_db.insert_data(table_name,host,user,password,database)
            elif operation=='2':
                op = input("What you want to do?\n1.Show Tables\n2.Describe Table\n3.Show Table_Data\n4.Only column Values\n>>")
                read.run(op,host,user,password,database)
            elif operation=='3':
                op = input("What you want to update?\n1.Serial number\n2.Name\n3.Age\n4.Job_role\n5.Email\n>>")
                if op=='5':
                    us.udemail()
                elif op=='4':
                    us.udjob()
                elif op=='3':
                    us.udage()
                elif op=='2':
                    us.udname()
                elif op=='1':
                    us.udsno()
                else:
                    print("Enter a valid entery!!!!!")
            elif operation=='4':
                op = int(input("Which deletion want to perform?\n1.row(value)\n2.column\n3.table\n>>"))
                if op==1 or op==2 or op==3:
                    deletion.run(op,host,user,password,database)
                else:
                    print("Enter valid operation")
            else:
                print("Enter valid operation!!!!!")
            num = 1
            con = input("Want to Continue?? Press Yes/Y/yes/y\n>>")
    else: 
        print("NOT CONNECTED TO ANY DATABASE")
    print('-'*90)
    print('THANK YOU!!!BYE')
