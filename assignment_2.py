from fastapi import FastAPI

app = FastAPI()

books = [
    {
        "id": 1,
        "title": "The Guide",
        "author": "R K Narayan",
        "genre": "Fiction",
        "language": "English",
        "available": True
    },
    {
        "id": 2,
        "title": "Wings of Fire",
        "author": "A P J Abdul Kalam",
        "genre": "Biography",
        "language": "English",
        "available": True
    },
    {
        "id": 3,
        "title": "Python Basics",
        "author": "Code Team",
        "genre": "Technology",
        "language": "English",
        "available": False
    },
    {
        "id": 4,
        "title": "Telugu Stories",
        "author": "Local Author",
        "genre": "Fiction",
        "language": "Telugu",
        "available": True
    },
    {
        "id": 5,
        "title": "Indian History",
        "author": "History Team",
        "genre": "History",
        "language": "English",
        "available": False
    },
    {
        "id": 6,
        "title": "Science Facts",
        "author": "Science Team",
        "genre": "Science",
        "language": "Hindi",
        "available": True
    }
]

@app.get("/")
def meessage():
    return {
        "message" : "Library API is running"
    }
@app.get("/books")
def get_all_books(genre : str | None = None):
    if genre is not None:
        return [book for book in books if book["genre"].lower() == genre.lower()]
    return books

@app.get("/books/{book_id}")
def get_book_by_id(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    return {"error": "Book not found"}
@app.get("/books-by-language")
def get_book_by_lang(language: str):
    return [book for book in books if book["language"].lower() == language.lower()]