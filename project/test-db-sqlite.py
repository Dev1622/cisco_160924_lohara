from book_db import Book,bookTablesCreate,readBookById,createBook,deleteBook,updateBook,readAllBooks

bookTablesCreate()

books = readAllBooks()
print(books)
