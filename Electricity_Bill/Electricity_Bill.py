#___________________________________________________________________PROJECT ON ELECTRICITY BILL_____________________________________________________________________________
import mysql.connector as sql , random , datetime as dt,sys
conn=sql.connect(host='localhost',user='root',passwd='<=======>')  #MYSQL PASSWORD REQUIRED.................................
c1=conn.cursor()
if conn.is_connected():
    print('Mysql database is connected successfully____________________________________________________________________________\n')
    c1.execute('create database if not exists EBS')
    c1.execute('USE EBS')
    c1.execute('create table if not exists newuser (username VARCHAR (100) primary key,password VARCHAR (100), confirmpasswd VARCHAR(100))')
    c1.execute('create table if not exists AddNewCustomer (accountno int primary key, bankname VARCHAR(25), address VARCHAR(25), bankbranch VARCHAR(25), name VARCHAR(100),areacode INT(6),phoneno bigint,email VARCHAR(25),boxid VARCHAR(25))')
    c1.execute('create table if not exists Transaction(accountno INT(10), unit INT(10), toda VARCHAR(25), totamt INT (10), GST INT(10), totalamt INT(10),p VARCHAR(25),foreign key (accountno) references AddNewCustomer (accountno))')
    print("INITIALISING.........................................\n")
    conn.commit()
    unit=random.randint(0,101)
    c='YES' or 'yes' or 'Yes'
    V='YES' or 'yes' or 'Yes'
    
    while c=='YES' or 'yes' or 'Yes':
        print('\n***************************************************************WELCOME TO ELECTRICITY BILLING SYSTEM***************************************************************\n')
        print(dt.datetime.now())
        print('1.NEW USER')
        print('2.EXISTING USER')
        print('3.EXIT\n')
        choice1=eval(input('++ENTER YOUR CHOICE:'))
        if choice1==1:
            username=input('\n>>Enter your username number:')
            password=input('>>Enter your password:')
            confirmpasswd=input('>>Confirm your password:')
            if password==confirmpasswd:
                info1="insert into newuser values('{}','{}','{}')".format(username,password,confirmpasswd) 
                c1.execute(info1)
                conn.commit()
                d=input('->>Do you want to continue?(yes or no):')
                if d.upper()=='YES':
                    continue
                else:
                    print('\nTHANK YOU!!! VISIT AGAIN!!!!!!!!!!!!!!')
                    sys.exit(0)
                print('\n')
                
            else:
                print('Your confirm password is incorrect')
                print('Try again.........\n')
                d=input('->>Do you want to continue?(yes or no):')
                if d.upper()=='YES':
                    continue
                else:
                    print('\nTHANK YOU!!! VISIT AGAIN!!!!!!!!!!!!!!')
                    sys.exit(0)
                
        elif choice1==2:
            username=input('>>>Enter your username:')
            password=input('>>>Enter your password:')
            info2="select * from newuser where username='{}' and password='{}'".format(username,password)
            c1.execute(info2)
            data=c1.fetchall()
            conn.commit()
            while V=='YES' or 'yes' or 'Yes':
                if any(data):
                    print('\n*********************MAIN MENU************************')
                    print('1.ACCOUNT SETTINGS')
                    print('2.TRANSACTION')
                    print('3.VIEW INDIVIDUAL CUSTOMER DETAILS')
                    print('4.VIEW ALL CUSTOMER DETAILS')#
                    print('5.TRANSACTION DETAILS')#
                    print('6.EXIT')
                    print('\n')
                    choice2=int(input('++ENTER YOUR CHOICE:'))
                    if choice2==1:
                        print('1.NEW CUSTOMER')
                        print('2.DELETING EXISTING ACCOUNT\n')
                        choice12=int(input('++ENTER YOUR CHOICE:'))
                        if choice12==1:
                            accountno=random.randrange(1000000,9999999,10)
                            print('\na)Your accountno is',accountno)
                            boxid=input('b)Enter your Meter ID:')
                            bank=input('c)Enter your BANK NAME:')
                            bankbranch=input('d)Enter your BANK BRANCH:')
                            name=input('e)Enter your name:')
                            address=input('f)Enter your address:')
                            areacode=int(input('g)Enter your area PINCODE:'))
                            phoneno=int(input('h)Enter your PHONE NUMBER:'))
                            email=input('i)Enter your EMAIL ID:')
                            info2="insert into AddNewCustomer values('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(accountno,bank,bankbranch,name,address,areacode,phoneno,email,boxid)
                            c1.execute(info2)
                            c1.execute("insert into Transaction (accountno) values('{}')".format(accountno))
                            conn.commit()
                            V=input('\n->>Do you want to continue?(yes or no):')
                            if V=='yes':
                                continue
                            else:
                                break

                        elif choice12==2:
                            acc=input('a)ENTER YOUR ACCOUNT NUMBER:')
                            c1.execute("Select*from AddnewCustomer where accountno='{}'".format(acc))
                            dta=c1.fetchall()
                            if any(dta):
                                c1.execute("delete from Transaction where accountno='{}'".format(acc))
                                c1.execute("delete from AddNewCustomer where accountno='{}'".format(acc))
                                conn.commit()
                                print(">>>Database updated.........")
                                print('\n>>>THANK YOU FOR USING OUR SOFTWARE.\n',acc,'ACCOUNT IS SUCCESFULLY DELETED...............\n')
                            else:
                                print("\n>>>>>>>>>>>Data base not found for Deletion...............................\nPlease insert data in Customer info.......")


                            V=input('\n->>Do you want to continue?(yes or no):')
                            if V.upper()=='YES':
                                continue
                            else:
                                break

                    elif choice2==2:
                        accountno=int(input('a)Enter your account number:'))
                        info10="select*from Transaction where accountno="+str(accountno)
                        c1.execute(info10)
                        data3=c1.fetchall()
                        if any(data3):
                            pass
                        else:
                            print("\n>>>>>>>>>>>Data base not found for Transaction...............................\nPlease insert data in Customer info.......")
                        for row in data3:
                            paid=row[6]
                            if paid=='yes':
                                print('\n>>>>>You have already paid the bill......................................................')
                                break

                            else:
                               
                                print('\n>>>>>Dear customer, you have used',unit,'units of electricity')
                                print('>>>>>One unit of current is 150 ruppees')
                                amount=150*unit
                                toda=dt.date.today()
                                deadline=dt.date(2022,1,30)
                                if deadline<toda:
                                    fine=(toda-deadline)*30
                                    totamt=int(amount+fine.days)
                                    print('>>>>>You have delayed for',fine/30,'.The fine per day is 30 ruppees.')
                                    GST=(15/100)*totamt
                                    totalamt=totamt+GST
                                    print('>>>>>Please payup ',totalamt,'ruppees including GST\n')
                                    p=input('\n------>Please enter YES to transact:')
                                    if p.upper()=='YES':
                                        print('\n>Transaction successful.....')
                                        print('>You have paid the bill.....')
                                    else:
                                        print('\n>>>>>Please pay the bill sooner................\n')

                                else:
                                    totamt=amount
                                    GST=int((15/100)*amount)
                                    totalamt=int(amount+GST)
                                    print('>>>>>Please payup',totalamt,'ruppees including GST')
                                    p=input('\na)Please enter YES to transact:')
                                    if p.upper()=='YES':
                                        info3="update Transaction set unit='{}',toda='{}',totamt='{}',GST='{}',totalamt={},p='{}' where accountno='{}'".format(unit,toda,totamt,GST,totalamt,p,accountno)
                                        c1.execute(info3)
                                        conn.commit()
                                        print('>>Transaction successful..')
                                        print('>>You have paid the bill..\n')
                                    else:
                                        print('\n>>>>>Please pay the bill sooner......................\n')
                                        info4="update Transaction set unit='{}',toda='{}',totamt={},GST='{}',totalamt='{}',p='{}' where accountno='{}'".format(unit,toda,totamt,GST,totalamt,p,accountno)
                                        c1.execute(info4)
                                        conn.commit()
                                        V=input('->>Do you want to continue?(yes or no):')
                                        if V=='yes':
                                            continue
                                        else:
                                            break

                    elif choice2==3:
                        accountno=int(input('a)Enter your Account number:'))
                        info4='select*from AddNewCustomer where accountno='+str(accountno)
                        c1.execute(info4)
                        datas1=c1.fetchall()
                        counts=c1.rowcount
                        print('\n')
                        if counts==0:
                            print('\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Record not found<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
                        else:
                            pass
                        for row in datas1:
                            print('1 .Account number:',row[0])
                            print('2 .Bankname:',row[1])
                            print('3 .Bankbranch:',row[2])
                            print('4 .Your meter device ID:',row[8])
                            print('5 .Residential adress:',row[4])
                            print('6 .Area code:',row[5])
                            print('7 .Phone number:',row[6])
                            print('8 .Email:',row[7])
                            info5='select*from Transaction where accountno='+str(accountno)
                            c1.execute(info5)
                            data2=c1.fetchall()
                            for row in data2:
                                print('9 .UNIT:',row[1])
                                print('10.PAID ON:',row[2])
                                print('11.Amount TO BE PAID WITHOUT GST:',row[3])
                                print('12.GST:',row[4])
                                print('13.Amount TO BE PAID INCLUDING GST:',row[5])

                        V=input('\n->>Do you want to continue?(yes or no):')

                        if V=='yes':
                            continue
                        else:
                            break
                    elif choice2==4:
                        c1.execute('select*from AddNewCustomer')
                        datak = c1.fetchall()
                        count = c1.rowcount
                        conn.commit()
                        print("Total No. of Records in main database: ",count)
                        print("{0:<22s}{1:<22s}{2:<22s}{3:<22s}{4:<22s}{5:<22s}{6:<22s}{7:<22s}".format('Accountno','Bankname','Bankbranch','Name','Address','Areacode','Phoneno','Meterid'))
                        print("_______________________________________________________________________________________________________________________________________________________________________")
                        for row in datak:
                            print("{0:<22s}{1:<22s}{2:<22s}{3:<22s}{4:<22s}{5:<22s}{6:<22s}{7:<22s}".format(str(row[0]),str(row[1]),str(row[2]),str(row[3]),str(row[4]),str(row[5]),str(row[6]),str(row[8])))
                        print('\n')

                    elif choice2==5:
                        info9='select accountno,totalamt from Transaction'
                        c1.execute(info9)
                        data2=c1.fetchall()
                        print('\n')
                        print("{0:<15s}{1:<15s}".format('Accountno','Total amount'))
                        for i in data2:
                            print("{0:<15s}{1:<15s}".format(str(i[0]),str(i[1])))
                        print('\n')
                        V=input('->>Do you want to continue?(yes or no):')
                        if V=='yes':
                            continue
                        else:
                            break
                    elif choice2==6:
                        print('THANK YOU !!! VISIT AGAIN !!!')
                        c='no'
                        break
                    else:
                        print("INVALID ENTRY........")
                else:
                    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Username/Password is Incorrect<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n')
                    k=input('->>Do you want to try again(yes or no):')
                    if k.upper()!=c:
                        print('THANK YOU!!! VISIT AGAIN!!!!!!!!!!!!!!\n')
                        sys.exit(0)
                    else:
                        break
            else:
                print('\nTHANK YOU!!!!VISIT AGAIN!!!!!')
                V='no'

        elif choice1==3:
            print('\nTHANK YOU!!! VISIT AGAIN!!!!!!!!!!!!!!')
            c='no'
            break

        else:
            print('INVALID ENTRY........')
            c=input('->>Do you want to try again?(yes or no):')
else:
    print('Mysql connection failed................................................')
