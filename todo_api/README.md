# 📝 Todo API (Django + DRF)

A simple **Task Management API** built with **Django REST Framework**.  
It allows users to **sign up, log in, and manage tasks** (CRUD operations, filtering by category and priority).

## Features
- User authentication (signup, login, logout)
- Create, Read, Update, Delete (CRUD) tasks
- Task filtering by:
  - `priority` (`important`, `normal`)
  - `category` (e.g. `work`, `personal`)
- Ownership: users can only manage their own tasks
- Auto-timestamps for tasks (`created_at`, `updated_at`)

| Method | Endpoint           | Description                 | Auth Required |
| ------ | ------------------ | --------------------------- | ------------- |
| POST   | `/api/signup/`     | Create new user             | ❌ No          |
| POST   | `/api/login/`      | Log in user (session/token) | ❌ No          |
| POST   | `/api/logout/`     | Log out user                | ✅ Yes         |
| GET    | `/api/tasks/`      | List all tasks (for user)   | ✅ Yes         |
| POST   | `/api/tasks/`      | Create a new task           | ✅ Yes         |
| GET    | `/api/tasks/<id>/` | Retrieve task by ID         | ✅ Yes         |
| PUT    | `/api/tasks/<id>/` | Update full task            | ✅ Yes         |
| PATCH  | `/api/tasks/<id>/` | Partially update task       | ✅ Yes         |
| DELETE | `/api/tasks/<id>/` | Delete task                 | ✅ Yes         |

You can filter tasks by priority or category:

/api/tasks/?priority=important

/api/tasks/?category=work


RUNNING TESTS WILL COVER:

User signup, login, logout

Task creation, listing, retrieval

Full update (PUT) and partial update (PATCH)

Task deletion

Filtering by priority and category

Authentication enforcement



todo_api/
│── tasks
│── todo_api
│──db.sqlite3
│── manage.py
│── README.md
│
├── tasks/                
│   ├── _pycache_       
│   ├── migrations   
│   ├── templates/       
│   ├── __init__.py       
│   ├── admin.py        
│   └── apps.py        
│   │──models.py
├   │──serializers.py   
│   │──tests.py
│   │──urls.py
│   │──views.py
│
└── todo_api/             
    ├── settings.py
    ├── urls.py
    └── wsgi.py
    │──__pycache__
    │──__init__.py
    │──asgi.py
    


EXAMPLE OF TASK JSON FILE
    {
  "id": 1,
  "title": "Finish Django project",
  "description": "Work on API endpoints",
  "category": "work",
  "priority": "important",
  "completed": false,
  "due_date": "2025-09-05",
  "owner": "john"
}
