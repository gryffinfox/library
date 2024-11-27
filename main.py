from book import Book, Library

print("Welcome to the library. What can I do for you today?\n")
inside = True

while inside:
    library = Library()
    reply = int(input
        ("Please type in a number from 1 to 6 to select an option.\n 1 - Add a book\n 2 - Borrow a book\n 3 - Bring back a book\n 4 - Check disponibility of a book\n 5 - List all disponible books\n 6 - List all checked out books\n"))
    if reply == 1:
        title = input("Type in the title of the book: ")
        new_book = Book.create_book(title)
        add_book = library.add_book_to_library(new_book.title)

    elif reply == 2:
        borrow_book = Library.borrow_book(book)

    elif reply == 3:
        return_book = Library.return_book(book)

    elif reply == 4:
        book = input("What is the title of the book you are searching for?")
        print(Library.is_book_availble(book))

    elif reply == 5:
        print("We have these books: ", Library.display_all_books)

    elif reply == 6:
        print("These books are borrowed: ", Library.display_all_borrowed_books)

    else:
        help = "yes or no"
        question = input(f"Do you want to stay? Write {help} ").strip()
        if question == "no":
            inside = False
        else:
            continue

print("Bye!")


        
