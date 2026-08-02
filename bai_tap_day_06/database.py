from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DB_URL = "mysql+pymysql://root:Qu4nd3ptr4i!@localhost:3306/book_db"

engine = create_engine(DB_URL)

LocalSession = sessionmaker(bind=engine)

def get_db():
    db = LocalSession()

    try: 
        yield db

    finally:
        db.close