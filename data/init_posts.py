# data/init_posts.py

posts = [
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