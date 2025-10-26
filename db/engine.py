import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

# 載入 .env 檔案中的環境變數 (這行在本機開發時非常有用)
load_dotenv()

# 從環境變數中讀取資料庫 URL
# Vercel 會自動設定 POSTGRES_URL
# 為了相容性，我們也檢查 DATABASE_URL
DATABASE_URL = os.getenv("POSTGRES_URL") or os.getenv("DATABASE_URL")

if DATABASE_URL is None:
    # 如果在雲端和 .env 中都找不到，就退回使用本地 SQLite 作為備用
    print("警告：未找到 POSTGRES_URL 或 DATABASE_URL 環境變數，將使用本地 SQLite 資料庫。")
    DATABASE_URL = "sqlite:///./blog.db"

# 建立 SQLAlchemy engine
# 如果 URL 以 'postgres://' 開頭，SQLAlchemy 會知道要使用 PostgreSQL
engine = create_engine(
    DATABASE_URL,
    # 如果是 SQLite，才需要這個參數
    **({"connect_args": {"check_same_thread": False}} if DATABASE_URL.startswith("sqlite") else {})
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()