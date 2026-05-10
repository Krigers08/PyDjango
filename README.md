# Sumsum Todo App

## Overview

Sumsum is a minimal Django-based todo application designed for authenticated user-specific task management. It provides a lightweight interface for creating, filtering, marking, and deleting todos while enforcing ownership at the model level.

## Application Purpose

The app is intended to demonstrate a standard Django CRUD workflow with authentication and user-specific data isolation. Each user has their own set of todos, and operations are restricted so that users can only affect their own records.

## Functional Summary

- User registration and login via Django authentication.
- Per-user todo items with the following fields:
  - `title`: task title
  - `done`: completion state
  - `priority`: priority rank (Low / Medium / High)
  - `category`: fixed category set (`work`, `personal`, `urgent`, `other`)
- Todo list filtering:
  - show or hide completed todos
  - search by title substring
- Todo operations:
  - create new todo items
  - toggle completion state
  - delete individual todos
  - bulk update selected todos (mark done, mark undone, delete)

## Key Components

- `todos/models.py`: defines the `Todo` model, including ownership, priority, category, and completion state.
- `todos/views.py`: implements the application logic for the todo list, create, toggle, delete, bulk update, and registration.
- `todos/urls.py`: maps routes to view functions for todo management and registration.
- `templates/`: holds the HTML templates for presentation.

## Run Instructions

1. Ensure python3-venv is installed (on Ubuntu/Debian systems):
   ```bash
   sudo apt install python3-venv
   ```
2. Create and activate a Python virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. Install Django and any project dependencies if not already installed:
   ```bash
   pip install django python-dotenv
   ```
3. Apply database migrations:
   ```bash
   python manage.py migrate
   ```
4. Start the development server:
   ```bash
   python manage.py runserver
   ```
5. Open the app in a browser:
   - `http://127.0.0.1:8000/todos/`

## Usage

1. Register a new user at `/todos/register/`.
2. After login, the todo list view loads at `/todos/`.
3. Create a todo using the form on the list page.
4. Use the checkbox or action buttons to toggle completion and delete items.
5. Use the search input to filter todos by title.
6. Use the show completed toggle to hide or reveal completed tasks.
7. For bulk actions, select todos and choose one of the bulk controls.

## Notes

- Authentication is required for all todo management actions.
- Ownership is enforced by `Todo.owner` and query filtering in views.
- If you run this app against Supabase/PostgREST with PostgreSQL, do not expose Django internal tables through the public API.
- See `postgres/README.md` for PostgreSQL/PostgREST hardening guidance.
