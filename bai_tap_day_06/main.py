from fastapi import FastAPI, Depends, HTTPException
from database import get_db, engine
from Schemas import BookCreate, BookResponse
from sqlalchemy.orm import Session
from models import Book

book_db = []
book_id_counter = 1

app = FastAPI()

@app.post('/books', response_model=BookResponse, status_code=201)
def Create_book(book: BookCreate, db: Session = Depends(get_db)):
    new_book = Book(**book.model_dump())
    book_db.append(new_book)
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book


@app.get('/books/{id}', response_model=BookResponse, status_code=200)
def get_book_by_id(id, db: Session = Depends(get_db)):
    product = db.query(Book).filter(Book.id == id).first()
    if not product: 
        raise HTTPException(status_code=404, detail="Book not found")
    else:
        return product