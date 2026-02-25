class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True

    def display(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN: {self.isbn}")
        print(f"Availability: {'Available' if self.is_available else 'Not Available'}")


class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def display(self):
        print(f"Name: {self.name}")
        print(f"Member ID: {self.member_id}")
        print("Borrowed Books:")
        for book in self.borrowed_books:
            print(f"- {book.title}")


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, title, author, isbn):
        book = Book(title, author, isbn)
        self.books.append(book)

    def add_member(self, name, member_id):
        member = Member(name, member_id)
        self.members.append(member)

    def borrow_book(self, member_id, book_isbn):
        member = self.find_member(member_id)
        book = self.find_book(book_isbn)

        if member is None:
            print("Member not found.")
            return
        if book is None:
            print("Book not found.")
            return
        if not book.is_available:
            print("Book is not available.")
            return

        member.borrowed_books.append(book)
        book.is_available = False
        print(f"{member.name} has borrowed {book.title}.")

    def return_book(self, member_id, book_isbn):
        member = self.find_member(member_id)
        book = self.find_book(book_isbn)

        if member is None:
            print("Member not found.")
            return
        if book is None:
            print("Book not found.")
            return
        if book not in member.borrowed_books:
            print("Member has not borrowed this book.")
            return

        member.borrowed_books.remove(book)
        book.is_available = True
        print(f"{member.name} has returned {book.title}.")

    def find_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None

    def find_book(self, book_isbn):
        for book in self.books:
            if book.isbn == book_isbn:
                return book
        return None


# Example usage
library = Library()

library.add_book("The Great Gatsby", "AbdulSamad", "9780743273565")
library.add_book("To Kill a Mockingbird", "Ali", "9780061120084")

library.add_member("aslam", "12345")
library.add_member("smaid", "67890")

library.borrow_book("12345", "9780743273565")
library.borrow_book("67890", "9780061120084")

library.return_book("12345", "9780743273565")

library.books[0].display()
library.members[0].display()