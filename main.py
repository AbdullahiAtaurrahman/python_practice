# import dependencies
from fastapi import FastAPI
from uuid import UUID

# An endpoint is generally path as in file path

# initiate fastapi
app = FastAPI()

# create empty array which stores books for the library app
books = {}
book_data = {"id":0,"title":"", "author":"", "year":0,"pages":0,"language":""}

# app method using fastapi, this is the homepage(an endpoint). Get requests from server when endpoint is called
@app.get("/")
def home():
    return "Welcome to my first API page"

# app method using fastapi, this is the /books path(an endpoint). Get requests from server when endpoint is called
@app.get("/books")
def get_books():
    return books

# app method using fastapi, this is the /books/{dynamically} path(an endpoint). Get requests from server when endpoint is called
@app.get("/books/{id}")
def get_books_by_id(id: str):
    book = books.get(id)   
    if not book: 
        return {"error": "Book not found"}

    return book

# app method using fastapi, this is the /books/{dynamically} path(an endpoint). send requests to server when endpoint is called
@app.post("/books")
def add_book(
    title: str, author: str, year: int, pages: int, language: str
):
    new_book = book_data.copy()
    new_book["id"] = str(UUID(int = books.len()+ 1))
    new_book["title"] = title
    new_book["author"] =author
    new_book["year"] = year
    new_book["pages"] = pages
    new_book["language"] = language

    books[new_book["id"]] = new_book

    return {"message" :"added a new book", "data": new_book}

