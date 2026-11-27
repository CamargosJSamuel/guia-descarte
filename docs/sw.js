/* Service worker: guarda o guia no aparelho para abrir sem internet. */
const V='guia-c1cba259fd';
const CORE=['./','index.html','manifest.webmanifest','icon-192.png','icon-512.png','apple-touch-icon.png'];
self.addEventListener('install',e=>{e.waitUntil(caches.open(V).then(c=>c.addAll(CORE)).then(()=>self.skipWaiting()))});
self.addEventListener('activate',e=>{e.waitUntil(caches.keys().then(k=>Promise.all(k.filter(x=>x!==V).map(x=>caches.delete(x)))).then(()=>self.clients.claim()))});
self.addEventListener('fetch',e=>{
  const r=e.request;if(r.method!=='GET')return;
  const u=new URL(r.url),mine=u.origin===location.origin,font=/fonts\.(googleapis|gstatic)\.com$/.test(u.host);
  if(!mine&&!font)return;
  /* abre o que está guardado e atualiza em segundo plano (a versão nova aparece na próxima abertura) */
  e.respondWith(caches.match(r,{ignoreSearch:true}).then(m=>{
    const net=fetch(r).then(res=>{if(res.ok||res.type==='opaque'){const cp=res.clone();caches.open(V).then(c=>c.put(r,cp))}return res}).catch(()=>m||caches.match('index.html'));
    return m||net}))});
