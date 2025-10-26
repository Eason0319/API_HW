# db/engine.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# 使用 SQLite，資料庫檔案將會是專案根目錄下的 blog.db
SQLALCHEMY_DATABASE_URL = "sqlite:///./blog.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, 
    connect_args={"check_same_thread": False} # 這是 SQLite 的特殊要求
)

# 建立 SessionLocal 類別，之後我們會用它來建立資料庫 session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 建立 Base 類別，我們之後建立的 model 都會繼承它
Base = declarative_base()

# 提供一個 dependency，讓 FastAPI 可以在每個請求中取得資料庫 session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()