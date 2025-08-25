import mysql.connector as sqlctr
import sys
from datetime import datetime
u=input('Enter the username:')
p=input('Enter the password:')
mycon=sqlctr.connect(host='localhost',user='root',password='<=====>')#INSERT MSQL PASSWORD.....................INSERT MSQL PASSWORD.........................

if mycon.is_connected():
    cursor=mycon.cursor()
    cursor.execute("create database if not exists library")
    cursor.execute("use library")
    cursor.execute("create table if not exists books (SN integer primary key,Book_Name varchar(100),Quantity_Available integer,Price_Per_Day integer)")
    cursor.execute("create table if not exists Borrower \
                     (SN integer primary key,Borrowers_Name varchar(255),Book_Lent varchar(255),Date date\
                        ,Contact_no integer)")
    mycon.commit()
       
        
    
    def command(st):
        cursor.execute(st)
        
    def fetch():
        data=cursor.fetchall()
        for i in data:
            for j in i:
                print('%10s'%j,end='\t')
            print()
    def all_data(tname):
        li=[]
        st="desc "+tname
        command(st)
        data=cursor.fetchall()
        for i in data:
            li.append(i[0])
        st='select * from '+tname
        command(st)
        print('\n')
        print("-----ALL_DATA_FROM-TABLE_"+tname+"_ARE------\n")
        print(tuple(li))
        fetch()

    def detail_burrower(name,contact):
        tup=("SN","borrowers_name","book_lent","date","contact_no")
        print('\n---Details for borrower '+name+'---\n')
        print(tup)
        st="select * from borrower where borrowers_name like '{}' and contact_no={}".format(name,contact)
        command(st)
        fetch()
    def days_between(d1,d2):
        d1=datetime.strptime(d1,"%Y-%m-%d")
        d2=datetime.strptime(d2,"%Y-%m-%d")
        global days
        days=abs((d2-d1).days)
    def price_book(days,book_name):
        st1="select Price_Per_Day from books where Book_Name='{}'".format(book_name)
        command(st1)
        data=cursor.fetchall()
        for i in data:
            global t_price
            t_price=int(i[0])*days
            print("\nNo.of days {} book is kept: {}".format(book_name,i[0]))
        print("Total fare for book "+book_name+"- ",t_price)
    def lend():
        flag="true"
        while flag=="true":
            print("\n___AVAILABLE BOOKS___\n")
            st0="select Book_Name from books where Quantity_Available >= 1"
            command(st0)
            fetch()
            st1="select count(*) from borrower"
            command(st1)
            data_sn=cursor.fetchall()
            for i in data_sn:
                SN=i[0]+1
                book_selected=str(input("Enter name of book from above list:"))
                borrowers_name=str(input("Enter borrowers name: "))
                date=str(input("Enter date(YYYY-MM-DD): "))
                contact=int(input("Enter contact no : "))
                st_insert="""insert into borrower values('{}',"{}",'{}',"{}",{})""".format(SN,borrowers_name,book_selected,date,contact)
                command(st_insert)
                st_quantity="select quantity_available from books where book_name='{}'".format(book_selected)
                command(st_quantity)
                data_quantity=cursor.fetchall()
            for quantity in data_quantity:
                qty=quantity[0]-1
                st_dec="update books set quantity_available={} where book_name='{}'".format(qty,book_selected)
                command(st_dec)
            dec=str(input("\nDo you want to add more records (Y/N): "))
            if dec.upper()=="Y":
                flag="true"
            else:
                flag="false"
    def borrowers():
        print("\n\n___OPTIONS AVAILABLE___\n\
\nEnter 1: To show details of all borrowers\nEnter 2: To check details of a particular borrower \nEnter 3: To calculate total fine of a borrower\
\nEnter 4: To go back \nEnter 5: To commit all the changes and exit\n")
        dec=input("Enter your choice-")
        if dec=="1":
            all_data("borrower")
        elif dec=="2":
            name=str(input("\nEnter borrower name-"))
            contact=str(input("Enter borrower contact no-"))
            detail_burrower(name,contact)
        elif dec=="3":
            tfine()
        elif dec=="4":
            action_list()
        elif dec=="5":
            close()
        borrowers()
    def tfine():
        name=str(input("\nEnter borrower name: "))
        contact=input("Enter borrower contact_no: ")
        detail_burrower(name,contact)
        st1="select book_lent from borrower where borrowers_name='{}' and contact_no={}".format(name,contact)
        command(st1)
        data=cursor.fetchall()
        for i in data:
            book_name=i[0]
            st2='select date from borrower where borrowers_name="{}" and book_lent="{}"'.format(name,book_name)
            command(st2)
            data1=cursor.fetchall()
            for date in data1:
                date_taken=date[0]
                date_return=str(input("\nEnter returning date for book {}(YYYY-MM-DD)-".format(book_name)))
                while date_return!=date_taken:
                    days_between(str(date_return),str(date_taken))
                    price_book(days,i[0])
                    print("\nEnter Y: if Rs.{} is paid and book is returned,\nEnter N: if fare is not paid and book is not returned.".format(t_price))
                    dec=str(input("\nEnter (Y/N) :"))
                    if dec.upper()=="Y":
                       # print(i[0])
                        st="select SN, Quantity_Available from books where Book_Name like '{}'".format(i[0])
                        command(st)
                        data2=cursor.fetchall()
                        for price in data2:
                            update("books","Quantity_Available",price[1]+1,price[0])
                            st_del="delete from borrower where borrowers_name='{}' and book_lent='{}'".format(name,book_name)
                            command(st_del)
                        break
                    else:
                        print("\n\nPLEASE PAY THE FARE AND RETURN THE BOOK AFTER READING.\n\n")
                        break
    def insert():
        print("_"*20+' ADD NEW BOOKS IN LIST'+"_"*20)
        print('\n')
        flag="true"
        while flag=="true":
            licol=[]
            li1=[]
            li_val=[]
            command("desc books")
            data=cursor.fetchall()
            for i in data:
                licol.append(i[0])
            command("select max(SN) from books")
            dta=cursor.fetchall()
            for j in dta:
                li_val.append(j[0]+1)
            for k in range(1,4):
                val=input("--Enter Book_Name-")
                qt=input("--Enter Quantity-")
                pric=input("--Enter Price_per _day-")
                li_val.append(val)
                li_val.append(qt)
                li_val.append(pric)
                li1.append(tuple(li_val))
                values=",".join(map(str,li1))
                st1="INSERT INTO books VALUES {}".format(values)
                command(st1)
                all_data("books")
                print("\nDATA INSERTED SUCCESSFULLY\n")
                break
            dec=input("Do you want to insert more data?(Y/N)-")
            if dec.upper()=="Y":
                flag="true"
            else:
                flag="false" 
                action_list()
    def update(tname,col1,post_value,pre_value):
        st=str("update %s set %s=%s where SN=%s")%(tname,col1,"%s","%s")%(post_value,pre_value)
        command(st)
        mycon.commit()
        all_data(tname)
        print("\nVALUE UPDATED SUCCESSFULLY")
        
    def close():
        mycon.commit()
        mycon.close()
        if mycon.is_connected():
            print("Still connected to localhost")
        else:
            print("\n\nConnection closed successfully...............................................................")
            sys.exit()
    def action_list():
        while 0>-1:
            print('\n')
            print('_'*20+' MAIN MENU '+'_'*20)
            print("""\nEnter 1: To view details of all available Books\n\
Enter 2: To check details of a particular book\nEnter 3: To lend a book \nEnter 4: To add new books in list \nEnter 5: To update data\
\nEnter 6: To view details of borrowers \nEnter 7: To commit all changes and exit""")
            dec=input('\nEnter your choice-')
            if dec=='1':
                all_data('books')
            elif dec=='2':
                tup=('SN','book_name','quantity_available','price_per_day')
                tup1=('SN','borrowers_name','book_lent','Date','contact_no')
                in1=str(input("Enter first name, last name or middle name of a book-"))
                print('\n___ALL DATA OF BOOK HAVING "{}" IN THEIR NAME FROM BOTH TABLE___'.format(in1))
                st=str('select * from books where book_name like "{}"'.format('%'+in1+'%'))
                st1=str('select * from borrower where book_lent like "{}"'.format('%'+in1+'%'))
                print('\n___DATA FROM TABLE BOOKS---\n')
                command(st)
                print(tup)
                fetch()
                print('\n___DATA FROM TABLE BORROWER___\n')
                command(st1)
                print(tup1,'\n')
                fetch()
            
            elif dec=='3':
                lend()
            elif dec=='4':
                insert()
            elif dec=='5':
                flag='true'
                while flag=='true':
                    tname='books'
                    li=[]
                    st1='desc '+tname
                    command(st1)
                    data=cursor.fetchall()
                    for i in data:
                        li.append(i[0])
                    all_data(tname)
                    print('\n-------Columns in table '+tname+' are')
                    print(li)
                    col1=str(input('Enter column name for modification from above list='))
                    lipo=['SN']
                    lipo.append(col1)
                    print(tuple(lipo))
                    st0='select SN , %s from books' %(col1)
                    command(st0)
                    fetch()
                    pre_value=str(input('Enter corresponding SN for the data to be changed-'))
                    post_value=str(input('Enter new value for column %s having SN %s-' % (col1,pre_value)))
                    update(tname,col1,post_value,pre_value)
                    pec=str(input('\nDo you want to change more data?(Y/N)-'))
                    if pec.upper()=='Y':
                        print('Y')
                        flag='true'
                    else:
                        flag='false'
                        action_list()
                    
            elif dec=='6':
                borrowers()
            elif dec=='7':
                close()
    if p=='password' and u=='user':             #CAN BE ALTERED...................SENSITIVE................
        print('_'*150)
        print("Successfully connected to localhost..LOADING.....")
        print('_'*150)
        print('\n')
        print("""####################WELCOME TO LIBRARY MANAGEMENT SYSTEM ###################""")
        action_list()
    else:
        print("\nINCORRECT PASSWORD.......\n"+'>'*70+'ACCESS DENIED'+'<'*70)
        sys.exit(0)
        
    

else:
    print("Error while connecting to localhost")               
         
                                                                         
        
          
  





