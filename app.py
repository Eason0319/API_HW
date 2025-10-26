# app.py (修正 import 路徑後)

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from contextlib import asynccontextmanager

from db.init_data import create_tables, init_db
from db.engine import SessionLocal
from routers import posts as post_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("應用程式啟動...")
    create_tables()
    db = SessionLocal()
    init_db(db) # 這裡的呼叫不變
    db.close()
    yield
    print("應用程式關閉...")

app = FastAPI(lifespan=lifespan)

app.include_router(post_router.router)

# --- 靜態檔案服務 (以下不變) ---
@app.get("/")
async def read_index():
    return FileResponse('static/index.html')

@app.get("/blog.html")
async def read_blog_html():
    return FileResponse('static/blog.html')

@app.get("/post.html")
async def read_post_html():
    return FileResponse('static/post.html')

app.mount("/", StaticFiles(directory="static", html=True), name="static")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=5000)