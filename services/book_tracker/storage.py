from uuid import uuid4

books_db = []

def add_book(book):
    book_dict = book.model_dump()
    book_dict["id"] = str(uuid4())
    books_db.append(book_dict)
    return book_dict

def get_books():
    return books_db

def get_book(book_id):
    return next((b for b in books_db if b["id"] == book_id), None)

def delete_book(book_id):
    global books_db
    books_db = [b for b in books_db if b["id"] != book_id]
