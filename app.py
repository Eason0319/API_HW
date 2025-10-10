import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles # 匯入 StaticFiles
from fastapi.responses import FileResponse  # 匯入 FileResponse

# 假設您的 postJson.py 和 static 資料夾都與 app.py 在同一層目錄
try:
    from postJson import post_list
except ImportError:
    # 如果 postJson.py 不存在，提供一個備用的空列表
    post_list = []

app = FastAPI(
    title="我的部落格 API",
    description="",
    version="1.0.0"
)

# --- API 路由 ---
# 這一部分是您原本的 API 邏輯

@app.get("/api/posts")
def get_all_posts():
    """
    回傳所有文章的列表。
    """
    return post_list

@app.get("/api/posts/{slug}")
def get_post_by_slug(slug: str):
    """
    根據 slug 取得單篇文章的資料。
    """
    # 使用 next() 找到第一個符合條件的項目並回傳，若找不到則回傳 None
    post = next((post for post in post_list if post.get('slug') == slug), None)
    if post:
        return post
    return {"error": "Post not found"}

# --- 靜態檔案服務 ---
# 這是新增的部分，用來提供前端 HTML/JS/CSS 檔案

# 處理根路徑，當使用者訪問 "http://localhost:5000/" 時，回傳 index.html
@app.get("/")
async def read_index():
    # FileResponse 會回傳一個檔案作為回應 
    return FileResponse('static/index.html')

# 為了讓 post.html 也能被正確訪問，可以明確為它建立一個路由
@app.get("/post.html")
async def read_post_html():
    return FileResponse('static/post.html')

@app.get("/api/posts/{slug}/comments")
def get_comments_for_post(slug: str):
    """
    根據文章 slug 取得該文章的所有留言。
    """
    # 先找到對應的文章
    post = next((p for p in post_list if p.get('slug') == slug), None)
    
    if post:
        # 如果文章存在，回傳它的 comments 陣列
        return post.get("comments", []) # 使用 .get 確保即使沒有 comments 鍵也不會出錯
    
    # 如果找不到文章，回傳 404 錯誤
    return {"error": "Post not found"}, 404

@app.get("/api/posts/{slug}/likes")
def get_likes_for_post(slug: str):
    """
    根據文章 slug 取得該文章的所有按讚者列表。
    """
    post = next((p for p in post_list if p.get('slug') == slug), None)
    if post:
        return post.get("likes", [])
    return {"error": "Post not found"}, 404
# 掛載 (mount) static 資料夾 
# 這行指令會讓 FastAPI 將 "static" 資料夾內的檔案作為靜態資源提供
# 例如，瀏覽器請求 /index.js 時，FastAPI 會回傳 static/index.js 這個檔案
# 注意：掛載的指令必須放在所有路由定義之後
app.mount("/", StaticFiles(directory="static", html=True), name="static")


# --- 啟動伺服器 ---

if __name__ == "__main__":
    # 因為現在是同源服務，理論上可以移除 CORS，但保留著也無妨
    uvicorn.run("app:app", port=5000, reload=True)