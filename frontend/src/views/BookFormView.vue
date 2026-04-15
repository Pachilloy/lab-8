<script setup>
import { computed, onMounted, reactive, ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { createBook, fetchBook, updateBook } from '../api'

const route = useRoute()
const router = useRouter()
const saving = ref(false)
const loading = ref(false)
const errorMessage = ref('')

const form = reactive({ title: '', author: '', genre: '', price: 0, year: new Date().getFullYear() })
const isEditMode = computed(() => Boolean(route.params.id))

const loadBook = async () => {
  if (!isEditMode.value) return
  loading.value = true
  try {
    const response = await fetchBook(route.params.id)
    Object.assign(form, response.data)
  } catch (error) {
    errorMessage.value = 'Не удалось загрузить выбранную запись.'
  } finally {
    loading.value = false
  }
}

const handleSubmit = async () => {
  saving.value = true
  errorMessage.value = ''
  const payload = { title: form.title, author: form.author, genre: form.genre, price: Number(form.price), year: Number(form.year) }
  try {
    if (isEditMode.value) {
      await updateBook(route.params.id, payload)
    } else {
      await createBook(payload)
    }
    router.push('/')
  } catch (error) {
    errorMessage.value = error.response?.data?.detail?.[0]?.msg || 'Ошибка при сохранении данных.'
  } finally {
    saving.value = false
  }
}

onMounted(loadBook)
</script>

<template>
  <section class="card stack-md">
    <div>
      <h2>{{ isEditMode ? 'Редактирование книги' : 'Добавление новой книги' }}</h2>
      <p class="muted">Форма отправляет данные напрямую в REST API.</p>
    </div>
    <p v-if="loading" class="alert">Загрузка записи...</p>
    <p v-if="errorMessage" class="alert alert--error">{{ errorMessage }}</p>
    <form class="form-grid" @submit.prevent="handleSubmit">
      <label><span>Название</span><input v-model="form.title" type="text" required minlength="2" maxlength="150" /></label>
      <label><span>Автор</span><input v-model="form.author" type="text" required minlength="2" maxlength="100" /></label>
      <label><span>Жанр</span><input v-model="form.genre" type="text" required minlength="2" maxlength="60" /></label>
      <label><span>Цена</span><input v-model="form.price" type="number" step="0.1" min="0.1" required /></label>
      <label><span>Год</span><input v-model="form.year" type="number" min="1900" max="2100" required /></label>
      <div class="form-actions">
        <button class="button button--primary" :disabled="saving" type="submit">{{ saving ? 'Сохранение...' : 'Сохранить' }}</button>
        <RouterLink to="/" class="button button--secondary">Вернуться к каталогу</RouterLink>
      </div>
    </form>
  </section>
</template>
