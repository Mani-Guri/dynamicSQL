import mysql.connector as c,check
mydb = c.connect(host="localhost",user="root",password="123456789",database="student")
cursor = mydb.cursor()
def udemail():
    sno = int(input("Enter the serial number = "))
    check = check.checker.result(sno)
    if check==True:
        email = input("Enter new email = ")
        update = f"update std set email='{email}' where sno={sno};"
        cursor.execute(update)
        mydb.commit()
        print("UPDATED!!!!")
    else:
        print("Enter a valid serial Number!!!!")
def udjob():
    sno = int(input("Enter the serial number = "))
    check = check.checker.result(sno)
    if check==True:
        job_role = input("Enter the Job_Role = ")
        update = f"update std set job_role='{job_role}' where sno={sno};"
        cursor.execute(update)
        mydb.commit()
        print("UPDATED!!!!")
    else:
        print("Enter a valid serial Number!!!!")
def udage():
    sno = int(input("Enter the serial number = "))
    check = check.checker.result(sno)
    if check==True:
        age = int(input("Enter the age = "))
        update = f"update std set age={age} where sno={sno}"
        cursor.execute(update)
        mydb.commit()
        print("UPDATED!!!!")
    else:
        print("Enter a valid serial Number!!!!")
def udname():
    sno = int(input("Enter the serial Number = "))
    check = check.checker.result(sno)
    if check==True:
        name = input("Enter the name = ")
        update = f"update std set name='{name}' where sno={sno}"
        cursor.execute(update)
        mydb.commit()
        print("UPDATED!!!!")
    else:
        print("Enter a valid serial Number!!!!")
def udsno():
    sno = int(input("Enter the serial number = "))
    check = check.checker.result(sno)
    if check==True:
        new_sno = int(input("Enter New serial number = "))
        new_check = check.checker.result(new_sno)
        if new_check==None:
            update = f"update std set sno={new_sno} where sno={sno}"
            cursor.execute(update)
            mydb.commit()
            print("UPDATED!!!!")
    else:
        print("Enter a valid serial Number!!!!")