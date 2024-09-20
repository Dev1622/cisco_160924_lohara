from book import Book
#2. books[]
books = []

#3. book_add(id, name)
def book_add(id, name, price,copies):
    global books
    book = Book(id, name, price,copies)
    books.append(book)
    print('book created successfully')
    return
#4. book_remove(id)
def book_remove(id):
    global books
    for book in books:
        if book.id == id:
            print(book)
            if input('Are you sure to delete the (yes/no)?').lower() == 'yes':
                books.remove(book)
                print('book deleted successfully!')
            return 
        #end if 
    #end for 
    print(f'No such id {id}')
# display book by id
def display_id(id):
    global books
    for book in books:
        if book.id == id:
            print(book)
# update book by id
def book_update(id,name):
    global books
    for book in books:
        if book.id == id:
            print(book)
            if ('Are you sure to update the book?(yes/no):').lower == 'yes':
                book.name = name
                print('book details updated succesfully!')
                return

def book_return(id, name, price):
    global books
    book = Book(id, name, price)
    books.append(book)
    print('book returned successfully')

#5. book_display()
def book_display():
    global books
    for book in books:
        print(book)