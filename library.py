class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(book, "added to library.")

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(book, "removed from library.")
        else:
            print("Book not found.")

    def issue_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(book, "issued successfully.")
        else:
            print("Book is not available.")

    def return_book(self, book):
        self.books.append(book)
        print(book, "returned successfully.")

    def display_books(self):
        print("\nAvailable Books:")
        for book in self.books:
            print(book)


# Create object
library = Library()

library.add_book("Python Programming")
library.add_book("Database Management")
library.add_book("Web Development")

library.display_books()

library.issue_book("Python Programming")

library.display_books()

library.return_book("Python Programming")

library.display_books()