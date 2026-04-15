<script setup>
defineProps({
  books: {
    type: Array,
    required: true
  }
})

const emit = defineEmits(['remove'])
</script>

<template>
  <div class="table-wrapper">
    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>Название</th>
          <th>Автор</th>
          <th>Жанр</th>
          <th>Год</th>
          <th>Цена</th>
          <th>Действия</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="book in books" :key="book.id">
          <td>{{ book.id }}</td>
          <td>{{ book.title }}</td>
          <td>{{ book.author }}</td>
          <td>{{ book.genre }}</td>
          <td>{{ book.year }}</td>
          <td>{{ book.price }} ₽</td>
          <td class="actions-cell">
            <RouterLink :to="`/edit/${book.id}`" class="button button--secondary">Изменить</RouterLink>
            <button class="button button--danger" @click="emit('remove', book.id)">Удалить</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>
