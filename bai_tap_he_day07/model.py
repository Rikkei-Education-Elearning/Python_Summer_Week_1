from sqlalchemy import Column, Integer, String
from database import Base


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    ten_sach = Column(String(255), nullable=False)
    tac_gia = Column(String(255), nullable=False)
    nam_xuat_ban = Column(Integer, nullable=False)
    so_luong = Column(Integer, nullable=False)