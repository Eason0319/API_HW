// index.js （ES Module + Top-Level Await）
const listEl = document.getElementById('list');

function cardHTML(p) {
  const author = p.author ?? '';
  const title = p.title ?? '無標題';
  const href = `/post.html?slug=${encodeURIComponent(p.slug || '')}`;
  return `
    <a class="block rounded-xl border border-slate-200 bg-white p-4 shadow-sm hover:shadow-md hover:-translate-y-0.5 transition"
       href="${href}">
      <h3 class="text-lg font-semibold line-clamp-2">${title}</h3>
      <p class="mt-1 text-sm text-slate-600">作者：${author}</p>
    </a>
  `;
}

try {
  listEl.textContent = '載入中…';
  const res = await axios.get('http://127.0.0.1:5000/api/posts', { timeout: 10000 });
  const posts = res.data;

  if (!Array.isArray(posts) || posts.length === 0) {
    listEl.innerHTML = '<div class="text-slate-500">目前沒有文章。</div>';
  } else {
    listEl.innerHTML = posts.map(p => cardHTML(p)).join('');
  }
} catch (err) {
  listEl.innerHTML = `<div class="text-rose-600">讀取失敗：${err.message}</div>`;
  console.error('列表載入錯誤', err);
}
