<template>
  <div class="app-shell">
    <header class="topbar">
      <div>
        <p class="eyebrow">Лабораторная работа №8</p>
        <h1>Интеграция frontend и backend</h1>
        <p class="subtitle">SPA-приложение Vue 3 для управления книгами через FastAPI REST API.</p>
      </div>
      <nav class="nav-actions">
        <RouterLink to="/" class="nav-link">Каталог</RouterLink>
        <RouterLink to="/create" class="nav-link nav-link--primary">Добавить книгу</RouterLink>
      </nav>
    </header>

    <main class="page-container">
      <RouterView />
    </main>
  </div>
</template>
