# app.py
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from contextlib import asynccontextmanager
from data.init_data import create_tables, init_db

from db.engine import SessionLocal, engine
from data.init_data import create_tables, init_db
from routers import posts as post_router

# 在應用啟動時執行的內容
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("應用程式啟動...")
    # 建立資料庫表格
    create_tables()
    # 建立一個 session 來初始化資料
    db = SessionLocal()
    init_db(db)
    db.close()
    yield
    print("應用程式關閉...")

app = FastAPI(lifespan=lifespan)

# 包含 API 路由
app.include_router(post_router.router)

# --- 靜態檔案服務 ---
@app.get("/")
async def read_index():
    return FileResponse('static/index.html')

@app.get("/blog.html")
async def read_blog_html():
    # 當使用者訪問 /blog.html 時，回傳 blog.html (文章列表頁)
    return FileResponse('static/blog.html')

@app.get("/post.html")
async def read_post_html():
    return FileResponse('static/post.html')

app.mount("/", StaticFiles(directory="static", html=True), name="static")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=5000)