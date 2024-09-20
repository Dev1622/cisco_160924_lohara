from book_db import Book,bookTablesCreate,readBookById,createBook,deleteBook,updateBook,readAllBooks

bookTablesCreate()

""" id = createBook(Book(title='f',notes='flask is web dev framework and python package'))
print(f'{id} is inserted')
id = createBook(Book(title='django',notes='django is also web dev framework and python package. It includes all the batteries.'))
print(f'{id} is inserted') """

books = readAllBooks()
print(books)