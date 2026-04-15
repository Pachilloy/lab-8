<script setup>
defineProps({
  stats: {
    type: Object,
    required: true
  }
})
</script>

<template>
  <section class="stats-grid">
    <article class="stat-card">
      <span class="stat-label">Всего книг</span>
      <strong class="stat-value">{{ stats.total_books }}</strong>
    </article>
    <article class="stat-card">
      <span class="stat-label">Средняя цена</span>
      <strong class="stat-value">{{ stats.average_price }} ₽</strong>
    </article>
  </section>
</template>
