# impor engine dari sqlalchemy
from sqlalchemy import create_engine

# impor sessionmaker untuk pembuat class atau cetak biru
from sqlalchemy.orm import sessionmaker, declarative_base

# menyimpan alamat database sqlite
DATABASE_URL = "sqlite:///./salon.db"

# membuat koneksi engine ke database
engine = create_engine(
    DATABASE_URL,
    # mengizinkan beberapa pekerja untuk menggunakan hal yang sama
    connect_args={"check_same_thread":False}
)

SessionLocal = sessionmaker(autocommit= False, autoflush= False, bind= engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()