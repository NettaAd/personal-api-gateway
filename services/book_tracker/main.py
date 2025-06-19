from fastapi import FastAPI

app = FastAPI()

@app.get("/books")
def get_books():
    return {"books": ["Atomic Habits", "Clean Code", "The Pragmatic Programmer"]}
