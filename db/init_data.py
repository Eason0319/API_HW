from sqlalchemy.orm import Session
from db.engine import engine, Base, SessionLocal
from models import authors, posts, comments, likes
from data.init_posts import posts as initial_posts_data # 從 init_posts.py 匯入資料

def init_db(db: Session):
    """
    檢查資料庫並從 init_posts.py 填入您的初始資料
    """
    # 檢查資料庫是否已有文章資料，如果有，就跳過初始化
    if db.query(posts.Post).first():
        print("資料庫已有文章，跳過初始化。")
        return

    print("資料庫為空，開始從 init_posts.py 填入您的初始資料...")

    # --- 1. 處理所有不重複的作者/使用者 ---
    all_user_names = set()
    # 從文章作者收集
    for post_data in initial_posts_data:
        all_user_names.add(post_data["author"])
    # 從留言作者收集
    for post_data in initial_posts_data:
        for comment_data in post_data["comments"]:
            all_user_names.add(comment_data["author"])
    # 從按讚者收集
    for post_data in initial_posts_data:
        for like_data in post_data["likes"]:
            all_user_names.add(like_data["name"])
    
    # 建立 Author 物件並存入資料庫
    author_map = {}
    for name in all_user_names:
        # 預設頭像
        profile_pic_url = f"https://i.pravatar.cc/50?u={name.replace(' ', '_')}"
        # 如果在 likes 列表裡有指定頭像，就使用它
        for p in initial_posts_data:
            for l in p["likes"]:
                if l["name"] == name and l.get("profilePic"):
                    profile_pic_url = l["profilePic"]
                    break
        
        author = authors.Author(name=name, profilePic=profile_pic_url)
        db.add(author)
        author_map[name] = author
    
    db.commit() # 提交以獲取所有作者的 ID

    # --- 2. 處理文章、留言和按讚 ---
    for post_data in initial_posts_data:
        post_author = author_map[post_data["author"]]
        
        # 建立 Post 物件
        new_post = posts.Post(
            slug=post_data["slug"],
            title=post_data["title"],
            content=post_data["content"],
            author_id=post_author.id
        )
        
        # 建立關聯的 Comment 物件
        comment_objects = []
        for comment_data in post_data["comments"]:
            comment_author = author_map[comment_data["author"]]
            comment_objects.append(
                comments.Comment(
                    text=comment_data["text"],
                    author_id=comment_author.id
                )
            )
        new_post.comments = comment_objects

        # 建立關聯的 Like 物件
        like_objects = []
        for like_data in post_data["likes"]:
            like_author = author_map[like_data["name"]]
            like_objects.append(
                likes.Like(author_id=like_author.id)
            )
        new_post.likes = like_objects

        db.add(new_post)

    db.commit() # 一次性提交所有文章和其關聯的留言/按讚
    print(f"成功匯入 {len(initial_posts_data)} 筆文章資料。")


def create_tables():
    Base.metadata.create_all(bind=engine)