# this class stores information about one book

class Book:
    def __init__(self, book_id, title, author, genre, total_copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.genre = genre
        self.total_copies = total_copies
        self.available_copies = total_copies   # Copies left in library
        self.borrow_count = 0                 # the times book was borrowed