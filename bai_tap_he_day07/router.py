from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from model import Book as BookModel
from schema import Book

router = APIRouter(prefix="/api/v1/books", tags=["Books"])


@router.post("/", response_model=Book)
def create_book(book: Book, db: Session = Depends(get_db)):
    new_book = BookModel(**book.model_dump())

    db.add(new_book)
    db.commit()
    db.refresh(new_book)

    return new_book


@router.get("/", response_model=list[Book])
def get_all_books(db: Session = Depends(get_db)):
    return db.query(BookModel).all()


@router.get("/{book_id}", response_model=Book)
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(BookModel).filter(BookModel.id == book_id).first()

    if not book:
        raise HTTPException(
            status_code=404,
            detail=f"Không tìm thấy sách với id: {book_id}"
        )

    return book


@router.put("/{book_id}", response_model=Book)
def update_book(book_id: int, new_book: Book, db: Session = Depends(get_db)):
    book = db.query(BookModel).filter(BookModel.id == book_id).first()

    if not book:
        raise HTTPException(
            status_code=404,
            detail=f"Không tìm thấy sách với id: {book_id}"
        )

    book.ten_sach = new_book.ten_sach
    book.tac_gia = new_book.tac_gia
    book.nam_xuat_ban = new_book.nam_xuat_ban
    book.so_luong = new_book.so_luong

    db.commit()
    db.refresh(book)

    return book


@router.delete("/{book_id}", response_model=Book)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(BookModel).filter(BookModel.id == book_id).first()

    if not book:
        raise HTTPException(
            status_code=404,
            detail=f"Không tìm thấy sách với id: {book_id}"
        )

    db.delete(book)
    db.commit()

    return book