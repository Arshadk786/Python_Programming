'''
Experiment No.7
Program to illustrate Python-MySQL database connectivity.
RollNo.: 20CO24
Name: Khan Arshad Abdulla
'''
import mysql.connector
'''
THEORY:

    MySQL is a relational database management system (RDBMS) developed by Oracle that is based on structured query 
language (SQL).

    A database is a structured collection of data. It may be anything from a simple shopping list to a picture gallery or 
a place to hold the vast amounts of information in a corporate network. In particular, a relational database is a digital store collecting data and organizing it according to the relational model. In this model, tables consist of rows and columns, and relationships between data elements all follow a strict logical structure. An RDBMS is simply the set of software tools used to actually implement, manage, and query such a database. 

    MySQL Connector/Python enables Python programs to access MySQL databases, using an API that is compliant with the 
Python Database API Specification v2.0 (PEP 249). It is written in pure Python and does not have any dependencies except for the Python Standard Library.

This module does not come built-in with Python. To install it type the below command in the terminal.
    pip install mysql-connector-python
'''

def insert(myc,r,n,a,m,p):
    query="insert into Student values('"+r+"','"+n+"','"+m+"','"+a+"',"+str(p)+")"
    print(query)
    try:
        myc.execute(query)
        myc.execute('commit')
        print('Record inserted successfully..')
    except Exception as e:
        print('Insertion failed..'+str(e))
    
def display(mycursor):
    query='select * from Student'
    mycursor.execute(query)
    for row in mycursor:
        print(row)
    
def update(mycursor,col,val,r):
    try:
        query = f"update student set {col} = '{val}' where RollNo = '{r}'"
        mycursor.execute(query)
        print("Record Updated successfully")
    except Exception as e:
        print("Updation Failed...",e)
        
def delete(mycursor,r):
    try:
        query = f"delete from student where RollNo = '{r}'"
        mycursor.execute(query)
        print("Record Deleted successfully")
    except Exception as e:
        print("Deletion failed...",e)

def main():
    mydb = mysql.connector.connect(host="localhost",user="root",passwd="@rshadK786")
    mycursor=mydb.cursor()
    mycursor.execute('use stud_mgmt')
    while True:
        print('\t\t\tMENU\n1. Insert.\n2. Display.\n3. Update.')
        print('4. Delete. \n5. Exit.')
        ch=int(input('Enter your choice:: '))
        if ch==5:
            break
        elif ch==1:
            r=input('Enter the Roll No: ')
            n=input('Enter The Name: ')
            m=input('Enter Mobile No: ')
            a=input('Enter The Address: ')
            p=float(input('Enter The Pointer: '))
            insert(mycursor,r,n,a,m,p)
        elif ch==2:
            display(mycursor)
        elif ch==3:
            col = input("Enter Column name: ")
            val = input("Enter Value of COlumn: ")
            r=input('Enter the Roll No: ')
            update(mycursor,col,val,r)
        elif ch==4:
            r=input('Enter the Roll No: ')
            delete(mycursor,r)
        else:
            print('Wrong choice...')

        
if __name__=='__main__':
    main()
    
'''
OUTPUT: 

			MENU
1. Insert.
2. Display.
3. Update.
4. Delete. 
5. Exit.
Enter your choice:: Enter the Roll No: Enter The Name: Enter Mobile No: Enter The Address: Enter The Pointer: insert into Student values('20CO24','Arshad','9090909090','Mumbai',9.8)
Record inserted successfully..
			MENU
1. Insert.
2. Display.
3. Update.
4. Delete. 
5. Exit.
Enter your choice:: ('20CO24', 'Arshad', '9090909090', 'Mumbai', 9.8)
			MENU
1. Insert.
2. Display.
3. Update.
4. Delete. 
5. Exit.
Enter your choice:: Enter the Roll No: Enter The Name: Enter Mobile No: Enter The Address: Enter The Pointer: insert into Student values('20CO15','Dilshad','9878978976','Govandi',8.2)
Record inserted successfully..
			MENU
1. Insert.
2. Display.
3. Update.
4. Delete. 
5. Exit.
Enter your choice:: Enter Column name: Enter Value of COlumn: Enter the Roll No: Record Updated successfully
			MENU
1. Insert.
2. Display.
3. Update.
4. Delete. 
5. Exit.
Enter your choice:: ('20CO15', 'Dilshad', '9878978976', 'Govandi', 9.5)
('20CO24', 'Arshad', '9090909090', 'Mumbai', 9.8)
			MENU
1. Insert.
2. Display.
3. Update.
4. Delete. 
5. Exit.
Enter your choice:: Enter the Roll No: Record Deleted successfully
			MENU
1. Insert.
2. Display.
3. Update.
4. Delete. 
5. Exit.
Enter your choice:: ('20CO24', 'Arshad', '9090909090', 'Mumbai', 9.8)
			MENU
1. Insert.
2. Display.
3. Update.
4. Delete. 
5. Exit.
Enter your choice:: 
Process finished with exit code 0

CONCLUSION: In this Experiment we have established connection between MySQL and python using  mysql-connector-python.We have performed CRUD (create, read, update and delete) operations on database (MySQL) using python
'''