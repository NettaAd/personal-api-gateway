from fastapi import FastAPI, HTTPException
from services.book_tracker.models import Book
from services.book_tracker.storage import add_book, get_books, get_book, delete_book
from services.book_tracker.logger import logger

app = FastAPI()

@app.get("/books")
def list_books():
    logger.info("Fetching all books")
    return {"books": get_books()}

@app.post("/books")
def create_book(book: Book):
    logger.info(f"Adding book: {book}")
    new_book = add_book(book)
    return new_book

@app.get("/books/{book_id}")
def read_book(book_id: str):
    book = get_book(book_id)
    if not book:
        logger.warning(f"Book not found: {book_id}")
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@app.delete("/books/{book_id}")
def remove_book(book_id: str):
    if not get_book(book_id):
        logger.warning(f"Tried to delete missing book: {book_id}")
        raise HTTPException(status_code=404, detail="Book not found")
    delete_book(book_id)
    logger.info(f"Deleted book: {book_id}")
    return {"message": "Book deleted"}
