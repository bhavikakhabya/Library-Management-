# library_main.py
from library_class import Library

lib = Library()

while True:
    print("""
==============================
        LIBRARY MENU
==============================
1.Add Book
2.Borrow Book
3.Return Book
4.Rank Books
5.Monthly Insights
6.Bar Chart
7.Pie Chart
8.Exit
""")

    choice = input("Enter your choice: ")

    if choice == "1":
        id = input("Book ID: ")
        title = input("Title: ")
        author = input("Author: ")
        genre = input("Genre: ")
        copies = int(input("Total Copies: "))
        lib.add_book(id, title, author, genre, copies)

    elif choice == "2":
        id = input("Book ID to borrow: ")
        lib.borrow_book(id)

    elif choice == "3":
        id = input("Book ID to return: ")
        lib.return_book(id)

    elif choice == "4":
        lib.rank_books()

    elif choice == "5":
        lib.monthly_insights()

    elif choice == "6":
        lib.bar_chart()

    elif choice == "7":
        lib.pie_chart()

    elif choice == "8":
        print("Thank you for using the Library!")
        break

    else:
        print("Invalid choice, Try again!")