class Book:
    total_books = 0  # class variable

    def __init__(self, title):
        self.title = title
        Book.increment_book_count()

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

    @classmethod
    def display_total_books(cls):
        print(f"Total books: {cls.total_books}")

# Adding books
book1 = Book("Python Basics")
book2 = Book("Advanced Python")
book3 = Book("python scientist")

# Display total books
Book.display_total_books()