from sqlalchemy import Column, Float, Integer, String
from .database import Base


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(150), nullable=False)
    author = Column(String(100), nullable=False)
    genre = Column(String(60), nullable=False)
    price = Column(Float, nullable=False)
    year = Column(Integer, nullable=False)
