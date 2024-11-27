
class Book:
    def __init__(self, title):
        self.title = title
    
    available = True

    def create_book(self):
        return Book(self.title)

    def set_book_available(self):
        return self.book.available == True

    def set_book_not_available(self):
        return self.book.available == False


class Library:
    books = []
    borrowed_books = []

    def add_book_to_library(self, title):
        self.books.append(title)
        return print("You added new book.")

    def borrow_book(self, book):
        if book in self.books:
            if self.book.avalable:
                book.set_book_not_available()
                self.borrowed_books.append(book)
                return print("You checked out this book")
            else:
                return print("Sorry, this book is not available.")
        else:
                return print("Sorry, we don't have this book.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.set_book_available
            self.borrowed_books.remove(book)
            return print("Thank you for bringing the book back!")
        else:
            if book in self.books:
                return print("This book was never checked out.")
            else:
                return print("This book doesn't belong to our library.")

    def display_all_books(self):
        return self.books

    def display_all_borrowed_books(self):
        return self.borrowed_books
    
    def is_book_availble(self, book):
        if book in self.books or book in self.borrowed_books:
            if book.available == True:
                return print("Book is available.") # TO DO: add formated string with the title
            else:
                return print("Book is not available.")
        else:
            return print("We don't have this book in our library.")
