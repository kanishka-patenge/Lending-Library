from asyncio.windows_events import NULL
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Book
import mysql.connector
# Create your views here.
def choice(request):
    return render(request,'choice.html')



def add(request):
    if request.session.has_key('username'):
        if request.method == 'POST':
            mydb = mysql.connector.connect(
                host = "localhost",
                user = "root",
                password = "",
                database = "project"
            )
            mycursor = mydb.cursor()
            bookid = request.POST['bookid']
            name = request.POST['name']
            author = request.POST['author']
            publisher = request.POST['publisher']
            copies = request.POST['copies']
            accno = request.POST['accno']
            mycursor.execute("insert into book(bookid,name,author,publisher,copies)VALUES('"+bookid+"','"+name+"','"+author+"','"+publisher+"','"+copies+"')")
            l = list(accno.split(","))
            for x in l:
                mycursor.execute("insert into book_details(bookid,accno)VALUES('"+bookid+"','"+x+"') ")
            mydb.commit()
            return render(request,'add.html')
        else:
            return render(request,'add.html')
    else:
        return render(request,'adminlogin.html')


def delete(request):
    if request.session.has_key('username'):
        if request.method == 'POST':
            mydb = mysql.connector.connect(
                host = "localhost",
                user = "root",
                password = "",
                database = "project"
            )
            mycursor = mydb.cursor()
            bookid = request.POST['bookid']
            mycursor.execute(" delete from book where bookid = '"+bookid+"' ")
            mydb.commit()
            return render(request,'delete.html')
        else:
            return render(request,'delete.html')
    else:
        return redirect('adminlogin')

def copiesadd(request):
    if request.session.has_key('username'):
        if request.method == 'POST':
            mydb = mysql.connector.connect(
                host = "localhost",
                user = "root",
                password = "",
                database = "project"
            )
            mycursor = mydb.cursor()
            bookid = request.POST['bookid']
            add = request.POST['add']
            accno = request.POST['accno']
            mycursor.execute(" update book set avl = avl+'"+add+"', copies = copies + '"+add+"' where bookid = '"+bookid+"' ")
            l = list(accno.split(","))
            for x in l:
                mycursor.execute("insert into book_details(bookid,accno)VALUES('"+bookid+"','"+x+"') ")
            mydb.commit()
            return render(request,'copiesadd.html',{'status':'Added Succefully'})
        else:
            return render(request,'copiesadd.html')
    else:
        return redirect('adminlogin')


def copiesremove(request):
    if request.session.has_key('username'):
        if request.method == 'POST':
            mydb = mysql.connector.connect(
                host = "localhost",
                user = "root",
                password = "",
                database = "project"
            )
            mycursor = mydb.cursor()
            bookid = request.POST['bookid']
            add = request.POST['add']
            accno = request.POST['accno']
            mycursor.execute("select avl from book where bookid = '"+bookid+"' ")
            result = mycursor.fetchone()
            result = list(result)
            a = result[0]
            a = int(a)
            add = int(add)
            if(a >= add):
                add = str(add)
                mycursor.execute(" update book set avl=avl - '"+add+"',copies = copies-'"+add+"' where bookid = '"+bookid+"' ")
                l = list(accno.split(","))
                for x in l:
                    mycursor.execute(" delete from book_details where accno = '"+x+"' ")
            else:
                return render(request,'copiesremove.html',{'status':'invalid credintials'})

            mydb.commit()
            return render(request,'copiesremove.html')
        else:
            return render(request,'copiesremove.html')
    else:
        return redirect('adminlogin')

def signup(request):
    if request.method == 'POST':
        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "project"
        )
        mycursor = mydb.cursor()
        name = request.POST['name']
        username = request.POST['username']
        password = request.POST['password']
        branch = request.POST['branch']
        year = request.POST['year']
        emailid = request.POST['emailid']
        contact = request.POST['contact']
        address = request.POST['address']
        mycursor.execute(" insert into student (name,username,password,branch,year,emailid,contact,address)VALUES('"+name+"','"+username+"','"+password+"','"+branch+"','"+year+"','"+emailid+"','"+contact+"','"+address+"') ")
        mydb.commit()
        return render(request,'stulogin.html')
    else:
        return render(request,'signup.html')

def stulogin(request):
    if request.method == 'POST':
        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "project"
        )
        mycursor = mydb.cursor()
        username = request.POST['username']
        password = request.POST['password']
        mycursor.execute(" select * from student where username = '"+username+"' and password = '"+password+"' ")
        result = mycursor.fetchone()
        if(result!=None):
            request.session['username']=username
            return redirect('stuhome')
        else:
            return render(request,'stulogin.html',{'status':'invalid credentials'})
    else:
        return render(request,'stulogin.html')

def adminlogin(request):
    if request.method == 'POST':
        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "project"
        )
        mycursor = mydb.cursor()
        username = request.POST['username']
        password = request.POST['password']
        mycursor.execute(" select * from admin where username = '"+username+"' and password = '"+password+"' ")
        result = mycursor.fetchone()
        if(result!=None):
            request.session['username']=username
            return redirect('add')
        else:
            return render(request,'adminlogin.html',{'status':'invalid credentials'})
    else:
        return render(request,'adminlogin.html')

def lend(request):
    if request.session.has_key('username'):
        if request.method == 'POST':
            mydb = mysql.connector.connect(
                host = "localhost",
                user = "root",
                password = "",
                database = "project"
            )
            mycursor = mydb.cursor()
            bookid = request.POST['bookid']
            username = request.POST['username']
            accno = request.POST['accno']
            date = request.POST['date']
            mycursor.execute(" update book_details set studentid = '"+username+"',doi = '"+date+"' where bookid = '"+bookid+"' and accno = '"+accno+"' ")
            #print("update book set avl = avl-1 where bookid = '"+bookid+"' ")
            mycursor.execute("update book set avl = avl-1 where bookid = '"+bookid+"' ")
            mydb.commit()
            return render(request,'lend.html')
        else:
            return render(request,'lend.html')
    else:
        return redirect('login')

def returnbook(request):
    if request.session.has_key('username'):
        if request.method == 'POST':
            mydb = mysql.connector.connect(
                host = "localhost",
                user = "root",
                password = "",
                database = "project"
            )
            mycursor = mydb.cursor()
            bookid = request.POST['bookid']
            username = request.POST['username']
            accno = request.POST['accno']
            mycursor.execute(" delete from book_details where bookid = '"+bookid+"' and accno = '"+accno+"' ")
            mycursor.execute(" insert into book_details(bookid,accno)VALUES ('"+bookid+"','"+accno+"') ")
            mycursor.execute("update book set avl = avl+1 where bookid = '"+bookid+"' ")
            mydb.commit()
            return render(request,'returnbook.html')
        else:
            return render(request,'returnbook.html')
    else:
        return redirect('adminlogin')

def stuhome(request):
    if request.session.has_key('username'):
        uname = request.session['username']
        print('studenthome')
        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "project"
        )
        mycursor = mydb.cursor()
        mycursor.execute("select * from book ")
        result = mycursor.fetchall()
        books = []
        for x in result:
            book = Book()
            book.bookid = x[0]
            book.name = x[1]
            book.author = x[2]
            book.publisher = x[3]
            book.copies = x[4]
            book.avl = x[5]
            books.append(book)
        return render(request, 'stuhome.html', {"username" : uname,'att':books})
    else:
        return render(request, 'stulogin.html', {})

def stulogout(request):
    try:
        del request.session['username']
    except:
        pass
    return redirect('stulogin')

def adminlogout(request):
    try:
        del request.session['username']
    except:
        pass
    return redirect('adminlogin')
