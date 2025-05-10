from typing import Union


class User:
    id: Union[int, None]
    name: str
    email: str
    password: str

    def __init__(self, id: Union[int, None], name: str, email: str, password: str):
        self.id = id
        self.name = name
        self.email = email
        self.password = password

    def __str__(self):
        return f"Name: {self.name}, Email: {self.email}"

class Book:
    id: Union[int, None]
    isbn: str
    author: str
    title: str
    pages: int

    def __init__(self, id: Union[int, None], isbn: str, author: str, title: str, pages: int):
        self.id = id
        self.isbn = isbn
        self.author = author
        self.title = title
        self.pages = pages

    def __str__(self):
        return f"ISBN: {self.isbn}, Author: {self.author}, Title: {self.title}, Pages: {self.pages}"