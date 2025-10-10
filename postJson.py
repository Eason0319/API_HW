post_list = [
    {
        "id": "1",
        "slug": "javascript-guide",
        "title": "JavaScript 入門到實踐",
        "author": "程式探險家",
        "content": """
            <h3>歡迎來到 JavaScript 的世界</h3>
            <p>JavaScript (JS) 是一種輕量級、直譯式或即時編譯的程式語言，具有頭等函式 (first-class functions)。它最廣為人知的身份是作為網頁的腳本語言，但它也被用於許多非瀏覽器的環境中，例如 Node.js、Apache CouchDB 和 Adobe Acrobat。JavaScript 是一種基於原型的、多範式的單執行緒動態語言，支援物件導向、指令式和宣告式 (例如函式語言程式設計) 的風格。</p>
            <p>在本篇文章中，我們將探討幾個核心概念：</p>
            <ul>
                <li><strong>變數與資料型別：</strong> 了解 <code>let</code>, <code>const</code>, <code>var</code> 的差異，以及數字 (Number)、字串 (String)、布林 (Boolean)、物件 (Object) 等基本型別。</li>
                <li><strong>函式與作用域：</strong> 函式是 JS 的一等公民，我們將學習如何宣告函式、箭頭函式 (arrow functions) 的用法以及什麼是作用域鏈 (Scope Chain)。</li>
                <li><strong>非同步處理：</strong> 透過 <code>async/await</code> 和 <code>Promise</code> 來處理非同步操作，這是現代前端開發中不可或缺的技能，尤其是在串接 API 時。</li>
            </ul>
            <p>掌握這些基礎後，您將能更自信地開始您的前端開發之旅。祝您學習愉快！</p>
        """,
        "comments": [
            { "id": "c1", "author": "訪客A", "text": "寫得太好了，淺顯易懂！" },
            { "id": "c2", "author": "路人B", "text": "原來這就是 Top-level-await，學到了。" },
            { "id": "c3", "author": "新手C", "text": "感謝分享！" }
        ],
        "likes": [
            { "name": "小明", "profilePic": "https://i.pravatar.cc/50?u=ming" },
            { "name": "花花", "profilePic": "https://i.pravatar.cc/400?img=45" }
        ]
    },
    {
        "id": "2",
        "slug": "css-is-awesome",
        "title": "CSS 的魔法",
        "author": "設計魔法師",
        "content": """
            <h3>CSS 不只是改變顏色和字體</h3>
            <p>層疊樣式表 (Cascading Style Sheets, CSS) 是一種用來為結構化文件（如 HTML 文件或 XML 應用）添加樣式（字型、間距和顏色等）的電腦語言。很多人以為 CSS 只能改變顏色和字體，但其實它可以做到更多！從 Flexbox、Grid 佈局到複雜的動畫效果，CSS 的潛力是無窮的。</p>
            <p>現代 CSS 的強大之處在於其版面配置系統。過去開發者需要依賴浮動 (floats) 和定位 (positioning) 來建立複雜的佈局，過程既痛苦又容易出錯。現在，我們有了更強大的工具：</p>
            <ul>
                <li><strong>Flexbox：</strong> 一維佈局模型，非常適合用來排列項目清單、導覽列等。</li>
                <li><strong>Grid：</strong> 二維佈局模型，可以同時處理欄和列，是建立複雜網格佈局的完美工具。</li>
            </ul>
            <p>如同本專案使用的 <strong>Tailwind CSS</strong>，它就是一個基於 CSS utility-first 概念的框架，讓我們可以直接在 HTML 中使用原子化的 class 來快速建構介面，而不必離開我們的 HTML 檔案。 這大大提升了開發效率。</p>
        """,
        "comments": [
            { "id": "c4", "author": "設計師D", "text": "Tailwind CSS 真的改變了我的工作流程！" }
        ],
        "likes": [
            { "name": "小明", "profilePic": "https://i.pravatar.cc/50?u=ming" },
            { "name": "設計師D", "profilePic": "https://i.pravatar.cc/50?u=designer_d" },
            { "name": "訪客A", "profilePic": "https://i.pravatar.cc/50?u=visitor_a" }
        ]
    },
    {
        "id": "3",
        "slug": "a-guide-to-apis",
        "title": "什麼是 API？給初學者的指南",
        "author": "數據傳教士",
        "content": """
            <h3>API：應用程式的溝通橋樑</h3>
            <p>API (Application Programming Interface) 就像是餐廳裡的服務生。您（前端應用程式）是顧客，您手上有一份菜單（API 文件），上面寫著您可以點哪些菜（可用的功能或資料）。您不需要知道廚房（後端伺服器）內部是如何運作的，只需要告訴服務生您要什麼。</p>
            <p>服務生（API）接收到您的請求後，會進入廚房，按照標準流程取得您點的餐點（資料），然後端到您的桌上。這個過程就是一次完整的 API 呼叫。前端與後端透過一個事先定義好的「協定」來溝通，確保雙方都能理解對方的需求與回應。</p>
            <p>在本專案中，我們定義了 REST API 風格的端點，例如 <code>GET /api/posts</code>。這是一個符合 REST 設計原則的請求，它利用 HTTP Method (GET) 和 URL 資源路徑 (/api/posts) 的組合，讓伺服器理解我們想要「取得所有文章」的資料。 這使得前後端的分工更加清晰，開發也更有效率。</p>
        """,
        "comments": [],
        "likes": []
    }
]