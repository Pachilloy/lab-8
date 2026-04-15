from pydantic import BaseModel, ConfigDict, Field


class BookCreate(BaseModel):
    title: str = Field(..., min_length=2, max_length=150)
    author: str = Field(..., min_length=2, max_length=100)
    genre: str = Field(..., min_length=2, max_length=60)
    price: float = Field(..., gt=0)
    year: int = Field(..., ge=1900, le=2100)


class BookUpdate(BaseModel):
    title: str | None = Field(None, min_length=2, max_length=150)
    author: str | None = Field(None, min_length=2, max_length=100)
    genre: str | None = Field(None, min_length=2, max_length=60)
    price: float | None = Field(None, gt=0)
    year: int | None = Field(None, ge=1900, le=2100)


class BookResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    author: str
    genre: str
    price: float
    year: int


class StatsResponse(BaseModel):
    total_books: int
    average_price: float
