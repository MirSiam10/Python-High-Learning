class Book:
    def __init__(self, title: str, author: str, isbn: str):
        if not self.validate_isbn(isbn):
            raise ValueError("ISBN must be exactly 13 digits")

        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True

    def checkout(self):
        if not self.is_available:
            return f"'{self.title}' is already checked out."

        self.is_available = False
        return f"You have checked out '{self.title}'."

    def return_book(self):
        if self.is_available:
            return f"'{self.title}' was not checked out."

        self.is_available = True
        return f"You have returned '{self.title}'."

    def get_info(self):
        status = "Available" if self.is_available else "Checked Out"
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Status: {status}"

    @staticmethod
    def validate_isbn(isbn: str):
        return isbn.isdigit() and len(isbn) == 13


class Library:
    name = "City Library"
    _books = []
    _checkouts = 0

    def __init__(self, name: str):
        self.name = name

    def add_book(self, book: Book):
        self._books.append(book)

    def find_book(self, title: str):
        for book in self._books:
            if book.title.lower() == title.lower():
                return book
        return None

    def checkout_book(self, title: str):
        book = self.find_book(title)

        if not book:
            return "Book not found."

        if not book.is_available:
            return "Book already checked out."

        book.checkout()
        Library._checkouts += 1
        return f"Checked out: {book.title}"

    def return_book(self, title: str):
        book = self.find_book(title)

        if not book:
            return "Book not found."

        return book.return_book()

    @classmethod
    def get_available_books(cls):
        return [book.title for book in cls._books if book.is_available]

    @classmethod
    def get_summary(cls):
        total_books = len(cls._books)
        available_books = len([b for b in cls._books if b.is_available])
        return f"{cls.name} | Total Books: {total_books} | Available: {available_books} | Total Checkouts: {cls._checkouts}"

    @staticmethod
    def is_valid_library_name(name: str):
        return len(name) > 3
    
lib = Library("DIU Library")

b1 = Book("Python Basics", "Guido", "1234567890123")
b2 = Book("AI Intro", "Andrew Ng", "9876543210123")

lib.add_book(b1)
lib.add_book(b2)

print(lib.checkout_book("Python Basics"))
print(lib.checkout_book("Python Basics"))  # already checked out

print(lib.return_book("Python Basics"))

print(Library.get_available_books())
print(Library.get_summary())








            