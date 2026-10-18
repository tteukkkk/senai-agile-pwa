// 1. Nome do cache (versionado para facilitar atualizações)
const CACHE_NAME = 'senai-pwa-cache-v1';
// 2. Lista de recursos para armazenar em cache
const urlsToCache = [
    '/', // Página inicial
    '/static/css/style.css', // Arquivo CSS principal
    // Adicione outras rotas e arquivos estáticos importantes
];
// 3. Evento de INSTALAÇÃO (ocorre quando o SW é registrado pela primeira vez)
self.addEventListener('install', event => {
    // Mantém o processo de instalação ativo até que o cache seja preenchido
    event.waitUntil(
        caches.open(CACHE_NAME) // Abre o cache com o nome definido
            .then(cache => cache.addAll(urlsToCache)) // Adiciona todos os recursos à cache
    );
});
// 4. Evento de FETCH (intercepta todas as requisições de rede)
self.addEventListener('fetch', event => {
    if (event.request.method !== 'GET') return;
    const url = new URL(event.request.url);
    if (url.origin !== self.location.origin || !['/', '/static/css/style.css'].includes(url.pathname)) return;
    // Responde à requisição
    event.respondWith(
        // Verifica se a requisição existe no cache
        caches.match(event.request)
            .then(response => {
                // Se encontrou no cache: retorna a versão em cache
                // Se não encontrou: busca na rede
                return response || fetch(event.request);
            })
    );
});
self.addEventListener('activate', event => {
    event.waitUntil(caches.keys().then(keys => Promise.all(keys.filter(key => key !== CACHE_NAME).map(key => caches.delete(key)))));
});
