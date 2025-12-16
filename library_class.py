# This class manages all books in the library.

import json #load n save krne ke liye book ko 
import csv #borrow and return 
import os #sahi se file read hone ke liye 
from book_class import Book 
import matplotlib.pyplot as plt


class Library:
    def __init__(self):
        self.books = {}        # All books stored here
        self.load_books()      # Load previous data if it is there

# Load and Save function

    def load_books(self):
        """Reads books from books.json into the program"""
        if os.path.exists("books.json"):
            with open("books.json", "r") as f:
                data = json.load(f)
                for item in data:
                    b = Book(
                        item["book_id"],
                        item["title"],
                        item["author"],
                        item["genre"],
                        item["total_copies"]
                    )
                    b.available_copies = item["available_copies"]
                    b.borrow_count = item["borrow_count"]
                    self.books[b.book_id] = b

    def save_books(self):
        """Saves books back to books.json"""
        data = []
        for b in self.books.values():
            data.append({
                "book_id": b.book_id,
                "title": b.title,
                "author": b.author,
                "genre": b.genre,
                "total_copies": b.total_copies,
                "available_copies": b.available_copies,
                "borrow_count": b.borrow_count
            })

        with open("books.json", "w") as f:
            json.dump(data, f, indent=4)

    def log_event(self, book_id, action):
        """Saves borrow/return actions to logs.csv"""
        with open("logs.csv", "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([book_id, action])

# BOOK OPERATIONS

    def add_book(self, book_id, title, author, genre, copies):
        """Add a new book to the library"""
        if book_id in self.books:
            print("Book ID already exists!")
            return

        b = Book(book_id, title, author, genre, copies)
        self.books[book_id] = b
        self.save_books()
        print("Book added successfully.")

    def borrow_book(self, book_id):
        """Borrow a book (copies decrease & borrow increases)"""
        if book_id not in self.books:
            print("Book ID not found!")
            return

        b = self.books[book_id]

        if b.available_copies == 0:
            print("No copies available!")
            return

        b.available_copies -= 1
        b.borrow_count += 1
        self.log_event(book_id, "BORROW")
        self.save_books()

        print(f"You borrowed: {b.title}")

    def return_book(self, book_id):
        """Return a borrowed book"""
        if book_id not in self.books:
            print("Book ID not found!")
            return

        b = self.books[book_id]
        b.available_copies += 1
        self.log_event(book_id, "RETURN")
        self.save_books()

        print(f"You returned: {b.title}")

# POPULARITY AND ANALYTICS

    def rank_books(self):
        """Show books in order of popularity (borrow_count)"""
        print("\n--- Popular Books (Most Borrowed First) ---")
        ranked = sorted(self.books.values(), key=lambda x: x.borrow_count, reverse=True)

        for b in ranked:
            print(f"{b.title} — Borrowed {b.borrow_count} times")

    def monthly_insights(self):
        """Very simple insight: how many borrow events happened"""
        total_borrows = 0

        if os.path.exists("logs.csv"):
            with open("logs.csv", "r") as f:
                for row in csv.reader(f):
                    if row[1] == "BORROW":
                        total_borrows += 1

        print(f"\nTotal borrow actions so far: {total_borrows}")

# Visuals

    def bar_chart(self):
        """Bar chart of book popularity"""
        titles = [b.title for b in self.books.values()]
        counts = [b.borrow_count for b in self.books.values()]

        plt.bar(titles, counts)
        plt.xticks(rotation=45)
        plt.title("Book Popularity (Bar Chart)")
        plt.show()

    def pie_chart(self):
        """Pie chart of genre popularity"""
        genre_data = {}

        for b in self.books.values():
            genre_data[b.genre] = genre_data.get(b.genre, 0) + b.borrow_count

        plt.pie(list(genre_data.values()), labels=list(genre_data.keys()), autopct="%1.1f%%")
        plt.title("Genre-wise Popularity")
        plt.show()