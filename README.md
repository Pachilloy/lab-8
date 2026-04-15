# Лабораторная работа №8 — Интеграция frontend и backend

Проект демонстрирует создание SPA-приложения на Vue 3 с интеграцией с REST API, разработанным в лабораторных работах №3 и №4. В качестве backend используется FastAPI-приложение с SQLite, а frontend реализован как отдельное клиентское приложение на Vue 3 + Vite.

## Структура проекта

- `backend/` — FastAPI REST API для управления каталогом книг
- `frontend/` — SPA-приложение Vue 3 для работы с backend
- `report_assets/` — изображения для отчёта

## Запуск backend

```bash
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

## Запуск frontend

```bash
cd frontend
npm install
npm run dev
```

## Реализованные функции

- получение списка книг с backend;
- отображение статистики (`/stats`);
- создание новой записи;
- редактирование книги;
- удаление книги;
- поиск по каталогу;
- обработка ошибок загрузки и валидации.
