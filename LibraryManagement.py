import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

lo=str(input("set file location -- "))
name=str(input('enter name of file -- '))
location=lo+'\\'+name+'.csv'


#List all book
def viewall():
    #print("===================")
    print("List of All Records")
    print("===================")
    df=pd.read_csv(location,index_col='admno')#"C:\\Users\\DELL\\Downloads\\students.csv"
    print(df)
    
#search a book
def search():
    
    #print("================")
    print("search a book")
    print("================")
    df=pd.read_csv(location,index_col='book')#"C:\\Users\\DELL\\Downloads\\students.csv"
    list1=list(df.index)
    
    book=str(input('name of book -- '))
    search=book in list1
    if search == True:
        print("================")
        print("yes , book is avaialable")
        row=book
        del df['quantity']
        z=df.loc[row, : ]
        print(z)
    else:
        print("================")
        print("sorry , book not available now")
        
#Delete Existing book
def deleterecord():
    #print("================")
    print("delete record")
    print("================")
    x=pd.read_csv(location,index_col='book')#"C:\\Users\\DELL\\Downloads\\students.csv" 
    print(x)
    print("1.for row deletion")
    print("2.for column deletion")
    p=int(input("enter 1 or 2 --  "))
    if p==1:
        y=input("enter book name -- ")
        z=x.drop(y,axis=0)
        print("================")
        print("Resulting Data")
        print(z)
    elif p==2:
        y=input("enter column name -- ")
        z=x.drop(y,axis=1)
        print("================")
        print("Resulting Data")
        print(z)
    
#graph of books
def graph():
    #print("================")
    print("type of graphs \n (1) line , (2)bar , (3)scatter ")
    print("================")
    choice=str(input("enter name of type of graph -- "))
    X=pd.read_csv(location)#"C:\\Users\\DELL\\Downloads\\students.csv"
    if choice== 'bar' :
        X.plot(kind='bar',x='book',y='quantity')
        plt.xlabel('NAME OF BOOKS')
        plt.ylabel('QUANTITY OF BOOKS')
        plt.show()
    elif choice== 'line':
        X.plot(x='book',y='quantity')
        plt.xlabel('NAME OF BOOKS')
        plt.ylabel('QUANTITY OF BOOKS')
        plt.show()
    elif choice== 'scatter':
        X.plot(kind='scatter',x='book',y='quantity')
        plt.xlabel('NAME OF BOOKS')
        plt.ylabel('QUANTITY OF BOOKS')
        plt.show()
        
#name and data of person
def searchname():
    #print("================")
    print("search name of person")
    print("================")
    df=pd.read_csv(location,index_col='Name')#"C:\\Users\\DELL\\Downloads\\students.csv"
    list1=list(df.index)
    
    name=str(input('name of individual -- '))
    ser=name in list1
    if ser == True:
        print("================")
        print("Yes ,data available")
        print("DATA - ")
        y=name
        del df['quantity']
        z=df.loc[y,:]
        print(z)
    else:
        print("================")
        print("data not available")
# adding new data
def adddata():
    global location
    print("adding new Records")
    print("===================")
    x=f=pd.read_csv('C:\\Users\\DELL\\Desktop\\students.csv')
    print(x)
    list1=[]
    num=str(input('do you want to enter new record (yes|no) -- '))
    while num != 'no':
        admno=int(input('enter admno -- '))
        name=str(input('enter name of student -- '))
        book=str(input('enter name of book -- '))
        quantity=int(input('enter total quantity of books -- '))
        list2=[admno,name,book,quantity]
        #print(list2)
        list1.append(list2)
        num=str(input('next record (yes|no) -- '))
    df=pd.DataFrame(list1,columns=['admno','Name','book','quantity'])
    #print(df)
    newdf=x.append(df,ignore_index=True)
    print(newdf)
    ans=str(input('DO YOU WANT TO SAVE UPDATED DATA IN NEW FILE (yes|no) -- '))
    if ans == 'yes':
        location=str(input("set file location -- "))
        filename=str(input("set file name -- "))
        newdf.to_csv(location+'\\'+filename+'.csv',index=False)
        print("saved at location --",location,'named as ',filename)
    else:
        print('data updated shown but not saved ')  

print("\n")
print("\t \t \t LIBRARY MANAGEMENT SYSTEM")
print("Main Menu")
print("====================================")
print("1. Add a new book ")
print("2. Delete Existing book")
print("3. Search a book")
print("4. List of all data")
print("5. Graph [books vs quantity]")
print("6. Person data available")
print("7. Exit")
print("====================================")
print('\n')
choice = int(input('Enter your choice -- '))
print("====================================")
print('\n')
while choice < 7:
    if choice == 1 :
        adddata()
    elif choice == 2:
        deleterecord()
    elif choice == 3:
        search()
    elif choice == 4:
        viewall()
    elif choice == 5:
        graph()
    elif choice == 6:
        searchname()
    elif choice == 7:
        print("Software Terminated")
    print("==================================================")
    print('\n')
    print("Main Menu")
    print("====================================")
    print("1. Add a new book ")
    print("2. Delete Existing data")
    print("3. Search a book")
    print("4. List of all data")
    print("5. Graph [books vs quantity]")
    print("6. Person data available")
    print("7. Exit")
    print('\n')
    choice = int(input('Enter your choice -- '))
    


