# data/init_data.py

from sqlalchemy.orm import Session
from db.engine import engine, Base, SessionLocal
from models import authors, posts, comments, likes

# --- 初始資料來源 ---
# 我們將所有資料都定義在這裡
post_list = [
    {
        "slug": "javascript-guide",
        "title": "JavaScript 入門到實踐",
        "author": "程式探險家",
        "content": """
            <h3>歡迎來到 JavaScript 的世界</h3>
            <p>JavaScript (JS) 是一種輕量級、直譯式或即時編譯的程式語言...</p>
            <ul>
                <li><strong>變數與資料型別...</strong></li>
                <li><strong>函式與作用域...</strong></li>
                <li><strong>非同步處理...</strong></li>
            </ul>
            <p>掌握這些基礎後，您將能更自信地開始您的前端開發之旅。</p>
        """,
        "comments": [
            { "author": "設計魔法師", "text": "寫得太好了，淺顯易懂！" },
            { "author": "數據傳教士", "text": "原來這就是 Top-level-await，學到了。" },
        ],
        "likes": [
            { "name": "小明", "profilePic": "https://i.pravatar.cc/50?u=ming" },
            { "name": "小花", "profilePic": "https://i.pravatar.cc/400?img=45" }
        ]
    },
    {
        "slug": "css-is-awesome",
        "title": "CSS 的魔法",
        "author": "設計魔法師",
        "content": """
            <h3>CSS 不只是改變顏色和字體</h3>
            <p>層疊樣式表 (Cascading Style Sheets, CSS) 是一種用來為結構化文件添加樣式的電腦語言...</p>
            <p>如同本專案使用的 <strong>Tailwind CSS</strong>，它就是一個基於 CSS utility-first 概念的框架...</p>
        """,
        "comments": [
            { "author": "程式探險家", "text": "Tailwind CSS 真的改變了我的工作流程！" }
        ],
        "likes": [
            { "name": "小明", "profilePic": "https://i.pravatar.cc/50?u=ming" },
            { "name": "設計師D", "profilePic": "https://i.pravatar.cc/50?u=designer_d" },
            { "name": "訪客A", "profilePic": "https://i.pravatar.cc/50?u=visitor_a" }
        ]
    },
    {
        "slug": "a-guide-to-apis",
        "title": "什麼是 API？給初學者的指南",
        "author": "數據傳教士",
        "content": """
            <h3>API：應用程式的溝通橋樑</h3>
            <p>API (Application Programming Interface) 就像是餐廳裡的服務生...</p>
            <p>在本專案中，我們定義了 REST API 風格的端點...</p>
        """,
        "comments": [],
        "likes": []
    }
]

def init_db(db: Session):
    """
    檢查資料庫並從 post_list 填入初始資料
    """
    db = SessionLocal()
    try:
        # 檢查資料庫是否已有作者資料，如果有，就假設已初始化並跳過
        if db.query(authors.Author).first():
            print("資料庫已有資料，跳過初始化。")
            return

        print("資料庫為空，開始從 post_list 填入初始資料...")

        # --- 1. 處理所有不重複的作者 ---
        all_author_names = set()
        # 從文章作者收集
        for post_data in post_list:
            all_author_names.add(post_data["author"])
        # 從留言作者收集
        for post_data in post_list:
            for comment_data in post_data["comments"]:
                all_author_names.add(comment_data["author"])
        # 從按讚者收集 (假設按讚者也是作者)
        for post_data in post_list:
            for like_data in post_data["likes"]:
                all_author_names.add(like_data["name"])
        
        # 建立 Author 物件並存入資料庫
        author_map = {}
        for name in all_author_names:
            profile_pic_url = f"https://i.pravatar.cc/50?u={name}"
            # 找到按讚列表中的頭像來覆蓋預設值
            for p in post_list:
                for l in p["likes"]:
                    if l["name"] == name:
                        profile_pic_url = l["profilePic"]
                        break
            
            author = authors.Author(name=name, profilePic=profile_pic_url)
            db.add(author)
            author_map[name] = author
        
        db.commit() # 提交以獲取作者的 ID

        # --- 2. 處理文章、留言和按讚 ---
        for post_data in post_list:
            # 建立 Post 物件
            post_author = author_map[post_data["author"]]
            post = posts.Post(
                slug=post_data["slug"],
                title=post_data["title"],
                content=post_data["content"],
                author_id=post_author.id
            )
            db.add(post)
            db.commit() # 提交以獲取文章的 ID
            
            # 建立 Comment 物件
            for comment_data in post_data["comments"]:
                comment_author = author_map[comment_data["author"]]
                comment = comments.Comment(
                    text=comment_data["text"],
                    post_id=post.id,
                    author_id=comment_author.id
                )
                db.add(comment)

            # 建立 Like 物件
            for like_data in post_data["likes"]:
                like_author = author_map[like_data["name"]]
                like = likes.Like(
                    post_id=post.id,
                    author_id=like_author.id
                )
                db.add(like)
        
        db.commit() # 提交所有文章關聯的留言和按讚

        print("初始資料填入完成。")

    finally:
        db.close()

def create_tables():
    # 建立所有繼承 Base 的表格
    Base.metadata.create_all(bind=engine)