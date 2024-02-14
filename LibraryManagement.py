import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
"""

x=f=pd.read_csv("C:\\Users\\DELL\\Downloads\\students.csv" ,index_col='books')
print(x)
print("1.for row deletion")
print("2.for column deletion")
p=int(input("ooo"))

if p==1:
    y=input("")
    z=x.drop(y,axis=0)
    print(z)
elif p==2:
    y=input("")
    z=x.drop(y,axis=1)
    print(z)
    

"""
#List all book
def viewall():
    print("================")
    print("List of All Records")
    print("===================")
    f=pd.read_csv("C:\\Users\\DELL\\Downloads\\students.csv")
    print(f)

#search a book
def search():
    print("================")
    print("search a book")
    print("================")
    x=f=pd.read_csv("C:\\Users\\DELL\\Downloads\\students.csv",index_col='books')
    list1=list(f.index)
    
    book=str(input(''))
    ser=book in list1
    if ser == True:
        print("yes , it is avaialable")
    else:
        print("not")
#Delete Existing book
def deleterecord():
    print("================")
    print("delete record")
    print("================")
    x=f=pd.read_csv("C:\\Users\\DELL\\Downloads\\students.csv" ,index_col='books')
    print(x)
    print("1.for row deletion")
    print("2.for column deletion")
    p=int(input("ooo"))
    if p==1:
        y=input("")
        z=x.drop(y,axis=0)
        print(z)
    elif p==2:
        y=input("")
        z=x.drop(y,axis=1)
        print(z)
    

"""
def graph ():
    print("================")
    print("delete record")
    print("================")
    x=f=pd.read_csv("C:\\Users\\DELL\\Downloads\\students.csv" ,index_col='books')
"""
#graph of books
def graph():
    print("================")
    print("type of graphs \n (1) line , (2)bar")
    print("================")
    choice=str(input("enter type of graph"))
    X=pd.read_csv("C:\\Users\\DELL\\Downloads\\students.csv")
    if choice== 'bar':
        X.plot(kind='bar',x='books',y='quantity')
        plt.xlabel('NAME OF BOOKS')
        plt.ylabel('QUANTITY OF BOOKS')
        plt.show()
    elif choice== 'line':
        X.plot(x='books',y='quantity')
        plt.xlabel('NAME OF BOOKS')
        plt.ylabel('QUANTITY OF BOOKS')
        plt.show()
        

print("\n")
print("Main Menu")
print("==========")
print("1. Add a new book")#done
print("2. Delete Existing book")#done
print("3. search a book")#done
print("4. List all book")#done
print("5. graph of books")#done
print("6.Exit")
choice = int(input('Enter your choice'))
if choice == 1:
    """
    f=pd.read_csv("flepath")
    m=f.index
    n=f.columns
    n=n-1
    f.loc(m,n-1)=input('Enter name')
    f.loc(m,n)=input('Enter name')
    print("Record Saved")
    input("Press any key to continue..")
    """
elif choice == 2:
    deleterecord()
elif choice == 3:
        search()
elif choice == 4:
        viewall()
elif choice == 5:
        graph()
elif choice == 6:
    print("Software Terminated")


