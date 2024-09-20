import sqlite3

def connect():
    con = sqlite3.connect('book_db.db')
    return con 
def bookTablesCreate():
    sql = """CREATE TABLE IF NOT EXISTS books(
        id integer primary key AUTOINCREMENT,
        title varchar(255) not null,
        price integer not null,
        copies interger
    )"""
    con = connect()
    con.execute(sql)
    con.close()
    print("Database is connected and in sync.")

class Book:
    def __init__(self, id=None,
        title='',
        books='',
        copies=''):
        self.id = id 
        self.title = title 
        self.price = books
        self.copies = copies
    def __str__(self):
        return f'[{self.id},{self.title},{self.price},{self.copies}]'
    def __repr__(self):
        return self.__str__()

def createBook(book):
    sql = """INSERT INTO books(title, books)
    VALUES(?,?)"""
    params = (book.title, book.price, book.copies)
    con = connect()
    cur = con.cursor()
    cur.execute(sql,params)
    id = cur.lastrowid  #
    con.commit()
    con.close()
    return id           #

def readAllBooks():
    sql = """SELECT id,title, price FROM books"""
    params = tuple()
    con = connect()
    cur = con.cursor()
    response = cur.execute(sql,params)
    result = response.fetchall() #[rows], each row=[id,title,...]
    con.close()

    books = [] # [Note(id=row[0],title=row[1],books=row[2]) for row in result]
    for row in result:
        books.append(Book(id=row[0],title=row[1],
                price=row[2],copies=row[4]))
    return books 

def search(title, name):
    title = title.strip()
    name = name.strip()
    sql = """SELECT id,title, books FROM books
        WHERE ( ? == '' OR title=?) AND 
              ( ? == '' OR books like ('%' || ? || '%'))"""
    params = (title,title, name,name)
    con = connect()
    cur = con.cursor()
    response = cur.execute(sql,params)
    result = response.fetchall() #[rows], each row=[id,title,...]
    con.close()

    books = []
    for row in result:
        books.append(Book(id=row[0],title=row[1],
                books=row[2]))
    return books 

def updateBook(book):
    sql = """UPDATE books
    set title=?,books=?
    WHERE (id=?)"""
    params = (book.title, book.books,
              book.id,book.price,book.copies )
    con = connect()
    cur = con.cursor()
    cur.execute(sql,params)
    con.commit()
    con.close()
def deleteBook(id):
    sql = """DELETE from books
    WHERE (id=?)"""
    params = (id, )
    con = connect()
    cur = con.cursor()
    cur.execute(sql,params)
    con.commit()
    con.close()
    
def readBookById(id):
    sql = """SELECT id,title, books FROM books
    WHERE (id=?)"""
    params = (id,)
    con = connect()
    cur = con.cursor()
    response = cur.execute(sql,params)
    result = response.fetchone() #row=[id,title,...]
    con.close()

    if result != None:
        book = Book(id=result[0],title=result[1],
                price=result[2],copies=result[3])
    else:
        book = None 
    return book