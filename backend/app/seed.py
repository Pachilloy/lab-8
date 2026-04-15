from sqlalchemy.orm import Session
from .models import Book

SEED_BOOKS = [
    {"title": "Clean Code", "author": "Robert C. Martin", "genre": "Programming", "price": 42.5, "year": 2008},
    {"title": "Fluent Python", "author": "Luciano Ramalho", "genre": "Programming", "price": 55.0, "year": 2022},
    {"title": "The Pragmatic Programmer", "author": "Andrew Hunt", "genre": "Programming", "price": 48.9, "year": 2019},
]


def seed_books(db: Session) -> None:
    if db.query(Book).count() > 0:
        return
    for book in SEED_BOOKS:
        db.add(Book(**book))
    db.commit()
