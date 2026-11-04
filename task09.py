"""Task 09 — Library/Book/Member association and loan rules."""


class Book:
    def __init__(self, title, author):
        if not title or not author:
            raise ValueError("Book needs a title and author")
        self.title = title
        self.author = author
        self.is_available = True
        self.library = None
        self.borrowed_by = None


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        if not isinstance(book, Book):
            raise TypeError("Only Book objects can be added")
        if book.library is not None:
            raise ValueError("Book already belongs to a library")
        self.books.append(book)
        book.library = self

    def remove_book(self, book):
        if book not in self.books:
            raise ValueError("Book is not in this library")
        if not book.is_available:
            raise ValueError("Cannot remove a borrowed book")
        self.books.remove(book)
        book.library = None

    def search_book(self, title):
        return [
            book for book in self.books
            if title.casefold() in book.title.casefold()
        ]


class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if not isinstance(book, Book) or book.library is None:
            raise ValueError("Book is not registered in a library")
        if not book.is_available:
            raise ValueError("Book has already been borrowed")
        book.is_available = False
        book.borrowed_by = self
        self.borrowed_books.append(book)

    def return_book(self, book):
        if book not in self.borrowed_books or book.borrowed_by is not self:
            raise ValueError("This member did not borrow this book")
        self.borrowed_books.remove(book)
        book.borrowed_by = None
        book.is_available = True


def demo():
    library = Library("Central Library")
    books = [
        Book("Clean Code", "Robert Martin"),
        Book("Python Basics", "A. Author"),
        Book("Algorithms", "B. Author"),
    ]
    members = [Member("Ali"), Member("Vali"), Member("Sardor")]
    for book in books:
        library.add_book(book)
    for member, book in zip(members, books):
        member.borrow_book(book)
        print(member.name, "borrowed", book.title)
    members[0].return_book(books[0])
    print("Available:", books[0].is_available)
    print("Search:", [b.title for b in library.search_book("python")])


if __name__ == "__main__":
    demo()
