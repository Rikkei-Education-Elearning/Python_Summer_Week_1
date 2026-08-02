from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Float, String, Integer 


class Base(DeclarativeBase):
    pass

class Book(Base):
    __tablename__ = 'Books'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(255))
    author: Mapped[str] = mapped_column(String(50))
    price: Mapped[float] = mapped_column(Float)
    pages: Mapped[int] = mapped_column(Integer) 