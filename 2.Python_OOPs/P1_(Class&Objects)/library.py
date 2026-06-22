class Book :
    def __init__(self, title, author, pages, is_checked_out=False):
        if not title or not author:
            raise ValueError("Title and author cannot be empty.")
        if pages <= 0:
            raise ValueError("Pages must be a positive number.")
        self.title = title
        self.author = author
        self.pages = pages
        self.is_checked_out = is_checked_out

    def checked_out(self):
        if not self.is_checked_out:
            self.is_checked_out = True
            return f"{self.title} has been checked out."
        else:
            return f"{self.title} is already checked out."
    def return_book(self):
        if self.is_checked_out:
            self.is_checked_out = False
            return f"{self.title} has been returned."
        else:
            return f"{self.title} was not checked out."
    def get_info(self):
        return f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}, Checked Out: {self.is_checked_out}"
    
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 180)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 281)
book3 = Book("1984", "George Orwell", 328)
checkout_result = book1.checked_out()
print(checkout_result)
checkout_result = book1.checked_out()
print(checkout_result)
return_result = book1.return_book()
print(return_result)
print(book1.get_info())
print(book2.get_info())
print(book3.get_info())
