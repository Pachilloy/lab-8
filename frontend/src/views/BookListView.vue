<script setup>
import { computed, onMounted, ref } from 'vue'
import { deleteBook, fetchBooks, fetchStats } from '../api'
import StatsCards from '../components/StatsCards.vue'
import BookTable from '../components/BookTable.vue'

const books = ref([])
const stats = ref({ total_books: 0, average_price: 0 })
const loading = ref(true)
const errorMessage = ref('')
const query = ref('')

const loadData = async () => {
  loading.value = true
  errorMessage.value = ''
  try {
    const [booksResponse, statsResponse] = await Promise.all([fetchBooks(), fetchStats()])
    books.value = booksResponse.data
    stats.value = statsResponse.data
  } catch (error) {
    errorMessage.value = 'Не удалось загрузить данные с backend.'
  } finally {
    loading.value = false
  }
}

const filteredBooks = computed(() => {
  const value = query.value.trim().toLowerCase()
  if (!value) return books.value
  return books.value.filter((book) => [book.title, book.author, book.genre].some((field) => field.toLowerCase().includes(value)))
})

const handleDelete = async (id) => {
  const confirmDelete = window.confirm('Удалить выбранную книгу?')
  if (!confirmDelete) return
  try {
    await deleteBook(id)
    await loadData()
  } catch (error) {
    errorMessage.value = 'Ошибка при удалении записи.'
  }
}

onMounted(loadData)
</script>

<template>
  <section class="stack-lg">
    <StatsCards :stats="stats" />
    <section class="card stack-md">
      <div class="toolbar">
        <div>
          <h2>Каталог книг</h2>
          <p class="muted">Список записей получен из FastAPI backend.</p>
        </div>
        <input v-model="query" class="search" type="text" placeholder="Поиск по названию, автору, жанру" />
      </div>
      <p v-if="errorMessage" class="alert alert--error">{{ errorMessage }}</p>
      <p v-if="loading" class="alert">Загрузка данных...</p>
      <p v-else-if="filteredBooks.length === 0" class="alert">Записи не найдены.</p>
      <BookTable v-else :books="filteredBooks" @remove="handleDelete" />
    </section>
  </section>
</template>
