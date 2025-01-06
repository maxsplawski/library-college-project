class User:
    def __init__(self):
        print("To be implemented")

class Book:
    id: int|None
    isbn: str
    author: str
    title: str
    pages: int

    def __init__(self, id: int|None, isbn: str, author: str, title: str, pages: int):
        self.id = id
        self.isbn = isbn
        self.author = author
        self.title = title
        self.pages = pages

    def __str__(self):
        return f"ISBN: {self.isbn}, Author: {self.author}, Title: {self.title}, Pages: {self.pages}"