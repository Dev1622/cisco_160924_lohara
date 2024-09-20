from book_service import book_add, book_update, book_display, book_remove, display_id, book_return
#6. menu 
def menu():
    choice = int(input('''1-add book
2-delete book by id
3-display all books
4-display book by id
5-update book by id
6-return book
7-end                       
your choice:'''))
    if choice == 1:
        id = int(input('Enter book id:'))
        name = input('Enter book name:')
        price = int(input('Enter the price of the book:'))
        copies = input("Enter the no of copies:")
        book_add(id, name, price, copies)
        return
    elif choice == 2:
        id = int(input('Enter book id to delete:'))
        book_remove(id)
        return
    elif choice == 3:
        book_display()
        return
    elif choice == 4:
        id = int(input('Enter book id to display:'))
        display_id(id)
        return
    elif choice == 5:
        id = int(input("Enter book id:"))
        name = input("Enter book name:")
        book_update(id,name)
        return
    if choice == 6:
        id = int(input('Enter book id:'))
        name = input('Enter book name:')
        price = int(input('Enter the price of the book:'))
        book_return(id, name, price)
        return
    elif choice == 7:
        pass
        return
    else:
        print('Invalid menu')
    return choice

#7. menus 
def menus():
    choice = menu()
    while choice != 7:
        choice = menu()
    print('Thank you for using the app')