"""
You are building a Library Management System. 
Create a `Book` class with properties like `title`, `author`, and `isbn`. 
Write a method to display book details.
"""

class Library:
    def __init__(self, title, author, isbn):
        self.title = title 
        self.author = author 
        self.isbn = isbn 

    def display_book(self):
        print("The following are the book details:")
        print(f"Title: {self.title}\nAuthor: {self.author}\nISBN: {self.isbn}")

def main():
    book1 = Library("The Great Gatsby", "Fitzgerald", 11)
    book2 = Library("The Song of Achilles", "Miller", 12)
    book3 = Library("The Seven Husbands of Evelyn Hugo", "Reid", 13)

    book1.display_book()
    book2.display_book()
    book3.display_book()

main()