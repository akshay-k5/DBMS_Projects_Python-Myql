import mysql.connector as mcon
import sys

con = mcon.connect(host="localhost",port="3306",user="root",passwd="<=======>") ### ENTER YOUR MYQL PASSWORD
mycursor = con.cursor()
if con.is_connected():
    print("MySql DataBase is connected Successfully.")
    print("__________________________________________WELCOME TO STUDENT DATABASE MANAGEMENT SYSTEM_________________________________________________")
    mycursor.execute("create database if not exists school_C")
    mycursor.execute("use school_C")
    mycursor.execute("create table if not exists user \
                     (uname varchar(20) primary key,upwd varchar(20)\
                     ,utype char(7),ustatus char(50))")
    Q = "insert into user values ('User','1234','Admin','2022-2023 CS Batch')"  ## PASSWORD DETAILS
    #print(Q)
    try:                                     #Conditional
        mycursor.execute(Q)
    except:
        pass
#____________________________________Class table creation section__________________________________________________________________
    c1="create table if not exists class_1(Admission_num integer primary key,Name varchar(50),Division char(1),RollNo integer)"
    c2="create table if not exists class_2(Admission_num integer primary key,Name varchar(50),Division char(1),RollNo integer)"
    c3="create table if not exists class_3(Admission_num integer primary key,Name varchar(50),Division char(1),RollNo integer)"
    c4="create table if not exists class_4(Admission_num integer primary key,Name varchar(50),Division char(1),RollNo integer)"
    c5="create table if not exists class_5(Admission_num integer primary key,Name varchar(50),Division char(1),RollNo integer)"
    c6="create table if not exists class_6(Admission_num integer primary key,Name varchar(50),Division char(1),RollNo integer)"
    c7="create table if not exists class_7(Admission_num integer primary key,Name varchar(50),Division char(1),RollNo integer)"
    c8="create table if not exists class_8(Admission_num integer primary key,Name varchar(50),Division char(1),RollNo integer)"
    c9="create table if not exists class_9(Admission_num integer primary key,Name varchar(50),Division char(1),RollNo integer)"
    c10="create table if not exists class_10(Admission_num integer primary key,Name varchar(50),Division char(1),RollNo integer)"
    c11="create table if not exists class_11(Admission_num integer primary key,Name varchar(50),Division char(1),RollNo integer)"
    c12="create table if not exists class_12(Admission_num integer primary key,Name varchar(50),Division char(1),RollNo integer)"
    correction="create table if not exists edict(Admission_num integer,dates date,mobileno integer(10),gender char(1),minority char(1))"
    
    mycursor.execute(correction)
    mycursor.execute(c1)
    mycursor.execute(c2)
    mycursor.execute(c3)
    mycursor.execute(c4)
    mycursor.execute(c5)
    mycursor.execute(c6)
    mycursor.execute(c7)
    mycursor.execute(c8)
    mycursor.execute(c9)
    mycursor.execute(c10)
    mycursor.execute(c11)
    mycursor.execute(c12)
    con.commit()
    at = 1
    while at <= 3:
        at += 1
        uid = input("\nEnter User Name : ")    #DEFINED IN 11th line
        pwd = input("Enter User Password : ")   #DEFINED IN 11th line
        print('\n')
        utype = 'Admin'
        mycursor.execute("select * from user where uname = '{}' and upwd = '{}'".format(uid,pwd))
        data = mycursor.fetchone()
        count = mycursor.rowcount
        #print(count)    
        if count == 1:
            print("Login Successfully........................\n")
            print("________________________________________________Perform CRUD Operations_________________________________________________________________________________.\n")

    #--------------------------*CHOICES*-----------------------------
            while True:
                print('________________MAIN MENU________________\n')
                print("1.Enter 'I' for Insertion a New Record.")
                print("2.Enter 'U' for Update an Existing Record.")
                print("3.Enter 'R' for Removal an Existing Record.")
                print("4.Enter 'S' for Searching a Record in Main database.")
                print("5.Enter 'D' for Display All Records.")
                print("6.Enter 'C' for Display individual class record.")
                print("7.Enter 'E' for Exit the Program.")
                print("8.Enter 'A' for Update User details.")
                print('\n')
                ch = input("+Enter Your Option: ")
                print('\n')

    #--------------------------*TABLE CREATION*-----------------------------
                if ch == 'I' or ch == 'i':
                    ins = "create table if not exists students(\
    admission_num int(20) primary key,\
    name char(50) NOT NULL,class integer NOT NULL,rollno integer NOT NULL,division char(1) NOT NULL,dob date NOT NULL,gender char(1) NOT NULL,\
    mother_name char(50) NOT NULL,father_name char(50) NOT NULL,category varchar(10),minority varchar(5),\
    pwd_status varchar(20),address varchar(80) NOT NULL,mode_of_tran varchar(20),mob_num bigint NOT NULL,email_id varchar(50),aadhar_num bigint,adm_date date)"

                    #print(ins)

                    mycursor.execute(ins)

    #--------------------------*INSERTION OF RECORDS*-----------------------------
                    
            
                    print("___Insertion Operation__.\n")
                    admino= int(input("1. Enter student's Admission Number: "))
                    cname = input("2. Enter student's Name: ")
                    classs=int(input("3. Enter the class: "))
                    if 0>=classs or classs>12:
                        print('***********************Incorrect entry********************************')
                        sys.exit(0)
                    else:
                        pass
                    rolll=int(input('4. Enter the rollnumber:'))
                    div=input('5. Enter the division: ')
                    dob=input("6. Enter student's date of birth as (yyyy-mm-dd):")
                    datesinp="insert into edict (dates) values('{}')".format(dob)
                    try:
                        mycursor.execute(datesinp)
                        con.commit()
                    except:
                        print('***********************Incorrect entry********************************')
                        sys.exit(0)
                    
                    gender = input("7. Enter student's gender(M/F/T): ")
                    gen="insert into edict (gender) values('{}')".format(gender)
                    try:
                        mycursor.execute(gen)
                        con.commit()
                    except:
                        print('**********************Incorrect entry******************************')
                        sys.exit(0)
                    mname = input("8. Enter student's mother's name: ")
                    fname = input("9. Enter student's father's name: ")
                    cat = input("10.Enter student's category: ")
                    minor = input("11.Enter if student belongs to minority section(Y/N): ")
                    mino="insert into edict (minority) values('{}')".format(minor)
                    try:
                        mycursor.execute(mino)
                        con.commit()
                    except:
                        print('**********************Incorrect entry******************************\nExiting.............')
                        sys.exit(0)
                    pwdis = input("12.Enter if student have disability (type of disability): ")
                    address=input("13.Enter the address:")
                    trans=input('14.Enter the mode of transport:')
                    mnum = int(input("15.Enter student's contact number: "))
                    email = input("16.Enter student's email_id: ")
                    ad_num = int(input("17.Enter student's addhar number: "))
                    adm_date = input("18.Enter student's admission date as (yyyy-mm-dd):")
                    datesinp2="insert into edict (dates) values('{}')".format(adm_date)
                    try:
                        mycursor.execute(datesinp2)
                        con.commit()
                    except:
                        print('**********************Incorrect entry******************************')
                        sys.exit(0)
                    cla=classs
                    if cla==1:
                        mycursor.execute("insert into class_1(Admission_num,name,Division,RollNo) values('{}','{}','{}','{}')".format(admino,cname,div,rolll))
                        con.commit()
                    elif cla==2:
                        mycursor.execute("insert into class_2(Admission_num,name,Division,RollNo) values('{}','{}','{}','{}')".format(admino,cname,div,rolll))
                        con.commit()
                    elif cla==3:
                        mycursor.execute("insert into class_3(Admission_num,Name,Division,RollNo) values('{}','{}','{}','{}')".format(admino,cname,div,rolll))
                        con.commit()
                    elif cla==4:
                        mycursor.execute("insert into class_4(Admission_num,Name,Division,RollNo) values('{}','{}','{}','{}')".format(admino,cname,div,rolll))
                        con.commit()
                    elif cla==5:
                        mycursor.execute("insert into class_5(Admission_num,Name,Division,RollNo) values('{}','{}','{}','{}')".format(admino,cname,div,rolll))
                        con.commit()
                    elif cla==6:
                        mycursor.execute("insert into class_6(Admission_num,Name,Division,RollNo) values('{}','{}','{}','{}')".format(admino,cname,div,rolll))
                        con.commit()
                    elif cla==7:
                        mycursor.execute("insert into class_7(Admission_num,Name,Division,RollNo) values('{}','{}','{}','{}')".format(admino,cname,div,rolll))
                        con.commit()
                    elif cla==8:
                        mycursor.execute("insert into class_8(Admission_num,Name,Division,RollNo) values('{}','{}','{}','{}')".format(admino,cname,div,rolll))
                        con.commit()
                    elif cla==9:
                        mycursor.execute("insert into class_9(Admission_num,Name,Division,RollNo) values('{}','{}','{}','{}')".format(admino,cname,div,rolll))
                        con.commit()
                    elif cla==10:
                        mycursor.execute("insert into class_10(Admission_num,Name,Division,RollNo) values('{}','{}','{}','{}')".format(admino,cname,div,rolll))
                        con.commit()
                    elif cla==11:
                        mycursor.execute("insert into class_11(Admission_num,Name,Division,RollNo) values('{}','{}','{}','{}')".format(admino,cname,div,rolll))
                        con.commit()
                    else:
                        mycursor.execute("insert into class_12(Admission_num,Name,Division,RollNo) values('{}','{}','{}','{}')".format(admino,cname,div,rolll))
                        con.commit()
                    
                    q = "insert into students (admission_num,name,class,rollno,division,\
    dob,gender,mother_name,father_name,category,minority,pwd_status,address,mode_of_tran,mob_num,email_id,aadhar_num,\
    adm_date) values ('{}','{}','{}','{}',\
    '{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')\
    ".format(admino,cname,classs,rolll,div,dob,gender,mname,fname,cat,minor,pwdis,address,trans,mnum,email,ad_num,adm_date)                             
                    mycursor.execute(q)
                    con.commit()
                    print('\n')
                    print("________________________________________Record is inserted Successfully.______________________________________________________\n")

    #--------------------------*UPDATION*-----------------------------               

                elif ch == 'U' or ch == 'u':
                    print("____________________________Updation of Record.____________________________\n")
                    admino= int(input("1. Enter student's current Admission Number: "))
                    cname = input("2. Enter student's Name: ")
                    classs=int(input("3. Enter the currently studying class: "))
                    if 0>=classs or classs>12:
                        print('***********************Incorrect entry********************************')
                        sys.exit(0)
                    else:
                        pass
                    rolll=int(input('4. Enter the rollnumber:'))
                    div=input('5. Enter the division: ')
                    dob=input("6. Enter student's date of birth as (yyyy-mm-dd):")
                    datesinp="insert into edict (dates) values('{}')".format(dob)
                    try:
                        mycursor.execute(datesinp)
                        con.commit()
                    except:
                        print('***********************Incorrect entry********************************')
                        sys.exit(0)
                    
                    gender = input("7. Enter student's gender(M/F/T): ")
                    gen="insert into edict (gender) values('{}')".format(gender)
                    try:
                        mycursor.execute(gen)
                        con.commit()
                    except:
                        print('**********************Incorrect entry******************************')
                        sys.exit(0)
                    mname = input("8. Enter student's mother's name: ")
                    fname = input("9. Enter student's father's name: ")
                    cat = input("10.Enter student's category: ")
                    minor = input("11.Enter if student belongs to minority section(Y/N): ")
                    mino="insert into edict (minority) values('{}')".format(minor)
                    try:
                        mycursor.execute(mino)
                        con.commit()
                    except:
                        print('**********************Incorrect entry******************************')
                        sys.exit(0)
                    pwdis = input("12.Enter if student have disability (type of disability): ")
                    address=input("13.Enter the address:")
                    trans=input('14.Enter the mode of transport:')
                    mnum = int(input("15.Enter student's contact number: "))
                    email = input("16.Enter student's email_id: ")
                    ad_num = int(input("17.Enter student's addhar number: "))
                    adm_date = input("18.Enter student's admission date as (yyyy-mm-dd):")
                    datesinp2="insert into edict (dates) values('{}')".format(adm_date)
                    try:
                        mycursor.execute(datesinp2)
                        con.commit()
                    except:
                        print('**********************Incorrect entry******************************')
                        sys.exit(0)
                    
                    
                    qry =  "update students set name='{}',class={},rollno={},division='{}',\
    dob='{}',gender='{}',mother_name='{}',father_name='{}',category='{}',minority='{}',pwd_status='{}',address='{}',mode_of_tran='{}',mob_num={},email_id='{}',aadhar_num={},\
    adm_date='{}' where admission_num={}".format(cname,classs,rolll,div,dob,gender,mname,fname,cat,minor,pwdis,address,trans,mnum,email,ad_num,adm_date,admino)
                    
                    
                    try:
                        mycursor.execute(qry)
                        query10="update class_{} set name='{}',Division='{}',RollNo={} where  Admission_num='{}'".format(classs,cname,div,rolll,admino)
                        mycursor.execute(query10)
                        mycursor.execute(qry)
                        con.commit()
                        print("\nRecord is updated Successfully.............................")
                        
                    except:
                        print("Record doesnot exists for updation..........................")
                        pass
                    print('\n')

    #--------------------------*DELETION*-----------------------------                   

                elif ch == 'R' or ch == 'r':
                    print("_______________________________Removal of Record.____________________________________________\n")
                    admino= int(input("1.Enter Student's Admission Number: "))
                    checkla=int(input("2.Enter the class: "))
                    if 0>=checkla or checkla>12:
                        print('***********************Incorrect entry********************************')
                        sys.exit(0)
                    else:
                        pass
                    qry = "delete from students where admission_num = '{}' and class='{}'".format(admino,checkla)
                    mycursor.execute('select*from students')
                    data2=mycursor.fetchall()
                    count1=mycursor.rowcount
                    mycursor.execute(qry)
                    con.commit()
                    mycursor.execute('select*from students')
                    data3=mycursor.fetchall()
                    count2=mycursor.rowcount
                    #print(count1,count2)
                    if count1>count2:
                        print("_________________________Record is deleted Successfully._____________________________")
                    else:
                        print('Record does not exists for deletion......................')
                    print('\n')

                    con.commit()
                    if checkla==1:
                        mycursor.execute("delete from class_1 where Admission_num='{}'".format(admino))
                        con.commit()
                    elif checkla==2:
                        mycursor.execute("delete from class_2 where Admission_num='{}'".format(admino))
                        con.commit()
                    elif checkla==3:
                        mycursor.execute("delete from class_3 where Admission_num='{}'".format(admino))
                        con.commit()
                    elif checkla==4:
                        mycursor.execute("delete from class_4 where Admission_num='{}'".format(admino))
                        con.commit()
                    elif checkla==5:
                        mycursor.execute("delete from class_5 where Admission_num='{}'".format(admino))
                        con.commit()
                    elif checkla==6:
                        mycursor.execute("delete from class_6 where Admission_num='{}'".format(admino))
                        con.commit()
                    elif checkla==7:
                        mycursor.execute("delete from class_7 where Admission_num='{}'".format(admino))
                        con.commit()
                    elif checkla==8:
                        mycursor.execute("delete from class_8 where Admission_num='{}'".format(admino))
                        con.commit()
                    elif checkla==9:
                        mycursor.execute("delete from class_9 where Admission_num='{}'".format(admino))
                        con.commit()
                    elif checkla==10:
                        mycursor.execute("delete from class_10 where Admission_num='{}'".format(admino))
                        con.commit()
                    elif checkla==11:
                        mycursor.execute("delete from class_11 where Admission_num='{}'".format(admino))
                        con.commit()
                    else:
                        mycursor.execute("delete from class_12 where Admission_num='{}'".format(admino))
                        con.commit()
                        
                    
                    
    #--------------------------*SEARCHING*-----------------------------               

                elif ch == 'S' or ch == 's':
                    print("__________________________________________Searching Operation.__________________________________________________")
                    admino = input("+Enter Student's Admission Number: ")              
                    qry = "select * from students where admission_num = {} ".format(admino)
                    #print(qry)
                    mycursor.execute(qry)
                    data = mycursor.fetchall()
                    count = mycursor.rowcount
                    if count==1:
                         print("Record is found Successfully.")
                         print("Total No. of Record:",count)
                         print("{0:<15s}{1:<15s}{2:<15s}{3:<15s}{4:<15s}{5:<15s}{6:<15s}{7:<15s}{8:<15s}{9:<15}".format('Adm_NO','Name','Class','Division','DOB','Gender','Mname','Fname','Category','pwd_status'))
                         print("____________________________________________________________________________________________________________________________________________________")
                         for row in data:
                          #print(row)
                             print("{0:<15s}{1:<15s}{2:<15s}{3:<15s}{4:<15s}{5:<15s}{6:<15s}{7:<15s}{8:<15s}{9:<15s}".format(str(row[0]),str(row[1]),str(row[2]),str(row[3]),str(row[4]),str(row[5]),str(row[6]),str(row[7]),str(row[8]),str(row[9])))
                    else:
                        print('\nRecord doesnot exists.................................')
                    print('\n')
                                
   

    #--------------------------*DISPLAY*-----------------------------                              

                elif ch == 'D' or ch == 'd':
                    print("_______________________________________________Display ALL Records._____________________________________________________________________\n")
                    qry = "select * from students"
                    mycursor.execute(qry)
                    data = mycursor.fetchall()
                    count = mycursor.rowcount
                    print("Total No. of Records in Student table: ",count)
                    print("{0:<15s}{1:<15s}{2:<15s}{3:<15s}{4:<15s}{5:<15s}{6:<15s}{7:<15s}{8:<15s}{9:<15}".format('Adm_NO','Name','Class','RollNO','Division','DOB','Gender','Fname','Mname','Category'))
                    print("____________________________________________________________________________________________________________________________________________________")
                    for row in data:
                        print("{0:<15s}{1:<15s}{2:<15s}{3:<15s}{4:<15s}{5:<15s}{6:<15s}{7:<15s}{8:<15s}{9:<15s}".format(str(row[0]),str(row[1]),str(row[2]),str(row[3]),str(row[4]),str(row[5]),str(row[6]),str(row[7]),str(row[8]),str(row[9])))
                    print('\n')
 #_______________________________*DISPLAY_INDIVIDUAL_CLASS_RECORD*________________
                elif ch == 'C' or ch == 'c':
                    print('________________________________Displaying Individual Class Records________________________________________________\n')
                    cla=int(input("+Enter the Class: "))
                    if 0>=cla or cla>12:
                        print('***********************Incorrect entry********************************')
                        sys.exit(0)
                    else:
                        pass
                    qry1="select * from class_{}".format(cla)
                    mycursor.execute(qry1)
                    data=mycursor.fetchall()
                    count=mycursor.rowcount
                    con.commit
                    if count>0:
                         print("Total No. of Records in Class{} table: {}".format(cla,count))
                         print('\n')
                         print("{0:<15s}{1:<15s}{2:<15s}{3:<15s}".format('Admission_NO','Name','Division','Roll_NO'))
                         print("__________________________________________________________________________________________")
                         for ros in data:
                             print("{0:<15s}{1:<15s}{2:<15s}{3:<15s}".format(str(ros[0]),str(ros[1]),str(ros[2]),str(ros[3])))
                         print('\n')
                    else:
                        print('\nRecord doesnot exists.................................')
                    print('\n')
                   
#______________________________________*USER_UPDATE_SECTION*___________________________
                elif ch=='A' or ch=='a':
                    print('__________________________________User Update______________________________________\n')
                    for i in range(1):
                        uid = input("\n1.Enter Current User Name : ")
                        pwd = input("2.Enter Current User Password : ")
                        print('\n')
                        mycursor.execute("select * from user where uname='{}' and upwd = '{}'".format(uid,pwd))
                        data = mycursor.fetchone()
                        count = mycursor.rowcount
                        con.commit()
                        if count == 1:
                            ptt=1
                            while ptt>0:
                                print('________USER MENU_______\n')
                                print("1.Enter 'A' for adding new user.")
                                print("2.Enter 'R' for removing existig user.")
                                print("3.Enter 'Q' for displaying user delails.")
                                print("4.Enter 'C' for exiting fom update section.\n")
                                ptt=0
                                
                                uh=input("+Enter your Option:")
                                if uh=='A' or uh=='a':
                                    uss=input("\n1.Enter new user name:")
                                    passs=input("2.Enter new password:")
                                    Q = "insert into user(uname,upwd) values ('{}','{}')".format(uss,passs)
                                    mycursor.execute(Q)
                                    con.commit()
                                    print("\nUser data updated successfully.........................")
                                elif uh=='R' or uh=='r':
                                    uss=input("\nEnter user name to be removed:")
                                    d="delete from user where uname='{}'".format(uss)
                                    mycursor.execute(d)
                                    con.commit()
                                    print("\nRemoved User data successfully.........................")
                                elif uh=='Q' or uh=='q':
                                    print("_______________________________________________Display ALL User Records._____________________________________________________________________\n")
                                    qry = "select * from user"
                                    mycursor.execute(qry)
                                    data = mycursor.fetchall()
                                    count = mycursor.rowcount
                                    print("Total No. of Records in User table: ",count)
                                    print('\n')
                                    print("{0:<15s}{1:<15s}{2:<15s}".format('Username','Password','User type'))
                                    print("________________________________________________________________________________________________")
                                    for row in data:
                                        print("{0:<15s}{1:<15s}{2:<15s}".format(str(row[0]),str(row[1]),str(row[2])))
                                    print('\n')
                                  
                            else:
                                ptt=0
                        else:
                            print("Incorrect password..................")
                            print(">>>>>>>>>>>>>>>>>>>>>>>>>Updation Failed<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                        
 #____________________________*EXIT SECTION*____________________________
                elif ch == 'E' or ch == 'e':
                    print("__________________________________________________________________________Exiting Program_______________________________________________________________.")
                    sys.exit(0)
                else:
                    print("Wrong Input. Try Again!!!!!")
                print('\n')
           
        else:
            print("Login Failed....................")
            if at !=4:
                if at==2:
                    print(at,'Attempts Left!!!')
                else:
                    print("1 Attempt Left!!!")
                print("\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Try Again<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                

else:
    print("MySql DataBase Connection Failed.Terminating....")
