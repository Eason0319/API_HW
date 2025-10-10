// post.js

// 取得主要容器的參考
const articleWrapperEl = document.getElementById('article-wrapper');
const sidebarContentEl = document.getElementById('sidebar-content');

// 解析 URL 中的 slug
const params = new URLSearchParams(location.search);
const slug = params.get('slug');

// --- 函式定義 ---

/**
 * 渲染文章內容到左側區塊
 */
function renderArticle(post) {
  const author = post.author ?? '';
  const title = post.title ?? '無標題';
  const body = post.content || '';

  articleWrapperEl.innerHTML = `
    <article class="rounded-xl border border-slate-200 bg-white p-5 shadow-sm">
      <h1 class="text-2xl md:text-3xl font-bold">${title}</h1>
      <p class="mt-1 text-sm text-slate-600">作者：${author}</p>
      <div class="prose prose-slate max-w-none mt-4">${body}</div>
      <button id="show-likes-btn" 
              class=" hover:bg-pink-500 text-black p-3 border-2 rounded-full shadow-lg focus:outline-none focus:ring-2 focus:ring-pink-400 transition">
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
          <path stroke-linecap="round" stroke-linejoin="round" d="M21 8.25c0-2.485-2.099-4.5-4.688-4.5-1.935 0-3.597 1.126-4.312 2.733-.715-1.607-2.377-2.733-4.313-2.733C5.1 3.75 3 5.765 3 8.25c0 7.22 9 12 9 12s9-4.78 9-12z" />
        </svg>
      </button>
      <button id="show-comments-btn" 
              class=" hover:bg-blue-500 text-black p-3 border-2 rounded-full shadow-lg focus:outline-none focus:ring-2 focus:ring-blue-400 focus:ring-opacity-75 transition">
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
          <path stroke-linecap="round" stroke-linejoin="round" d="M2.25 12.76c0 1.6 1.123 2.994 2.707 3.227 1.087.16 2.185.283 3.293.369V21l4.076-4.076a1.526 1.526 0 011.037-.443 48.282 48.282 0 005.68-.494c1.584-.233 2.707-1.626 2.707-3.228V6.741c0-1.602-1.123-2.995-2.707-3.228A48.394 48.394 0 0012 3c-2.392 0-4.744.175-7.043.513C3.373 3.746 2.25 5.14 2.25 6.741v6.018z" />
        </svg>
      </button>
    </article>
  `;
}

/**
 * 載入並渲染留言到右側區塊
 */
async function loadComments() {
  // 顯示載入中訊息
  sidebarContentEl.innerHTML = '<div class="p-4 bg-white rounded-xl shadow-sm text-slate-500">留言載入中…</div>';

  try {
    // 向新的 API 端點發送請求 (這裡沒有任何多餘的文字)
    const res = await axios.get(`/api/posts/${slug}/comments`);
    const comments = res.data;

    // 檢查是否有留言
    if (!Array.isArray(comments) || comments.length === 0) {
      sidebarContentEl.innerHTML = '<div class="p-4 bg-white rounded-xl shadow-sm text-slate-500">這篇文章目前沒有留言。</div>';
    } else {
      // 將留言資料轉換成 HTML
      const commentsHTML = comments.map(comment => `
        <div class="mb-3">
          <p class="font-semibold text-slate-800">${comment.author ?? '匿名'}</p>
          <p class="text-slate-600 text-sm">${comment.text ?? ''}</p>
        </div>
      `).join('');

      // 將組合好的 HTML 放入留言區塊
      sidebarContentEl.innerHTML = `
        <div class="p-4 bg-white rounded-xl shadow-sm">
          <h4 class="text-lg font-bold border-b pb-2 mb-3">留言 (${comments.length})</h4>
          ${commentsHTML}
        </div>
      `;
    }
  } catch (err) {
    // 如果 try 區塊發生任何錯誤，就在這裡顯示失敗訊息
    commentsWrapperEl.innerHTML = `<div class="p-4 bg-rose-100 text-rose-600 rounded-xl shadow-sm">留言讀取失敗：${err.message}</div>`;
    console.error('留言載入錯誤', err);
  }
}

async function loadLikes() {
  sidebarContentEl.innerHTML = '<div class="p-4 bg-white rounded-xl shadow-sm text-slate-500">按讚列表載入中…</div>';
  try {
    const res = await axios.get(`/api/posts/${slug}/likes`);
    const likes = res.data;

    if (!Array.isArray(likes) || likes.length === 0) {
      sidebarContentEl.innerHTML = '<div class="p-4 bg-white rounded-xl shadow-sm text-slate-500">這篇文章目前沒有人按讚。</div>';
    } else {
      const likesHTML = likes.map(like => `
        <div class="flex items-center gap-3 mb-3">
          <img src="${like.profilePic}" alt="${like.name}" class="w-10 h-10 rounded-full object-cover border-2 border-slate-200">
          <p class="font-semibold text-slate-800">${like.name ?? '匿名'}</p>
        </div>
      `).join('');

      sidebarContentEl.innerHTML = `
        <div class="p-4 bg-white rounded-xl shadow-sm">
          <h4 class="text-lg font-bold border-b pb-2 mb-3">按讚的用戶 (${likes.length})</h4>
          ${likesHTML}
        </div>
      `;
    }
  } catch (err) {
    sidebarContentEl.innerHTML = `<div class="p-4 bg-rose-100 text-rose-600 rounded-xl">按讚列表讀取失敗：${err.message}</div>`;
  }
}

// --- 主要執行邏輯 ---

if (!slug) {
  document.title = '參數缺失';
  articleWrapperEl.innerHTML = '<div class="text-rose-600">缺少 slug </div>';
} else {
  try {
    articleWrapperEl.innerHTML = '<div class="text-slate-500">載入中…</div>';
    const res = await axios.get(`/api/posts/${encodeURIComponent(slug)}`);
    const post = res.data;

    if (post.error) {
      throw new Error(post.error);
    }

    document.title = post.title || '文章';

    // 1. 渲染文章
    renderArticle(post);

    // 2. 找到剛剛渲染出來的按鈕
    const showCommentsBtn = document.getElementById('show-comments-btn');
    const showLikesBtn = document.getElementById('show-likes-btn');

    // 3. 為按鈕加上點擊事件監聽
    if (showCommentsBtn) {
      showCommentsBtn.addEventListener('click', loadComments);
    }
    if (showLikesBtn) {
      showLikesBtn.addEventListener('click', loadLikes); // 綁定新函式
    }

  } catch (err) {
    document.title = '找不到文章';
    articleWrapperEl.innerHTML = `<div class="text-rose-600">載入失敗或找不到文章：${err.message}</div>`;
    console.error('單篇載入錯誤', err);
  }
}