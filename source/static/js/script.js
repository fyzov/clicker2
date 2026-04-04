const pages = document.querySelectorAll('.page');

function handleRoute() {
    let hash = location.hash.slice(1) || 'home';
    if (!document.getElementById(hash)) hash = 'home';

    pages.forEach(p => p.classList.remove('active'));
    document.getElementById(hash)?.classList.add('active');
}

handleRoute();
addEventListener('hashchange', handleRoute);
