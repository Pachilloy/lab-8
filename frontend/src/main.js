import { createApp } from 'vue'
import { createRouter, createWebHistory } from 'vue-router'
import App from './App.vue'
import BookListView from './views/BookListView.vue'
import BookFormView from './views/BookFormView.vue'
import './style.css'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', component: BookListView },
    { path: '/create', component: BookFormView },
    { path: '/edit/:id', component: BookFormView, props: true }
  ]
})

createApp(App).use(router).mount('#app')
