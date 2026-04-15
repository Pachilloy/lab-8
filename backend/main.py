from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import func
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.database import Base, SessionLocal, engine, get_db
from app.seed import seed_books

app = FastAPI(
    title="Library API with Database",
    description="FastAPI-приложение с подключением SQLite базы данных для хранения книг.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)
with SessionLocal() as db:
    seed_books(db)


@app.get("/")
async def root():
    return {"message": "Library API is running"}


@app.get("/books", response_model=list[schemas.BookResponse])
async def read_books(db: Session = Depends(get_db)):
    return crud.get_books(db)


@app.get("/books/{book_id}", response_model=schemas.BookResponse)
async def read_book(book_id: int, db: Session = Depends(get_db)):
    book = crud.get_book(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@app.post("/books", response_model=schemas.BookResponse, status_code=201)
async def create_new_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    return crud.create_book(db, book)


@app.put("/books/{book_id}", response_model=schemas.BookResponse)
async def update_existing_book(book_id: int, book_data: schemas.BookUpdate, db: Session = Depends(get_db)):
    book = crud.update_book(db, book_id, book_data)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@app.delete("/books/{book_id}")
async def delete_existing_book(book_id: int, db: Session = Depends(get_db)):
    book = crud.delete_book(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"message": "Book deleted successfully", "book_id": book_id}


@app.get("/stats", response_model=schemas.StatsResponse)
async def get_statistics(db: Session = Depends(get_db)):
    total_books = db.query(func.count(models.Book.id)).scalar() or 0
    average_price = db.query(func.avg(models.Book.price)).scalar() or 0.0
    return {"total_books": total_books, "average_price": round(float(average_price), 2)}
