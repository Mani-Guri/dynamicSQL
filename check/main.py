import check,new_db,crud
Welcome = "Welcome to 'CRUD' operations of Mysql"
print(f"{Welcome:-^100}")
operation = input("Do You Have Database??\nPress = YES:NO\n>>")
if operation.lower() == 'yes':
    print("To Login into the Database Enter the Details:")
    host = input("Enter Your 'HOST' = ")
    user = input("Enter Your 'USER' = ")
    password = input("Enter Your 'PASSWORD' = ")
    database = input("Enter Your 'DATABASE' = ")
    db_check = check.connect_to_database1(host,user,password,database)
    if db_check == True:
        new_db.existed_database(host,user,password,database)

else:
    print("To Create New Database Enter the Details:")
    host = input("Enter Your 'HOST' = ")
    user = input("Enter Your 'USER' = ")
    password = input("Enter Your 'PASSWORD' = ")
    val = check.connect_to_database2(host,user,password)
    if val == True:
        database = input("Enter 'DATABASE' Name You Want To Give = ")
        new_db.cr_db(host,user,password,database)
        
#operation = input("TO OPERATE CRUD PRESS YES:NO\n>>")
#if operation.lower()=='yes':
crud.db_run(host,user,password,database)
#else:
#print("BYE!!!!!")
    


