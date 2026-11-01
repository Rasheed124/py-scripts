
# Todo List Application

## Project Overview

A Django-based Todo List application developed incrementally to practise Django concepts and software engineering principles.

## Technology Stack

- Python
- Django
- SQLite
- HTML
- CSS

## Project Structure

The project follows a modular Django structure, separating project configuration from application functionality.

### Project Structure Overview

![APPLICATION UI DESIGN VIEW](docs/images/todo-list-application-pictorial-ui-view.jpg)

![Project Core Structure](docs/images/project-core-feature-1.png)

![Project Application Structure](docs/images/project-core-feature-2.png)


## Development Stages

### Level 1 — Core Todo Functionality

- [x] Project initialization
- [x] Django configuration
- [x] Tasks application setup
- [x] Database model


### Database Design

#### Task Entity

| Field | Data Type | Description |
|---|---|---|
| id | BigAutoField | Primary key |
| title | CharField | Task title |
| description | TextField | Optional description |
| completed | BooleanField | Completion status |
| priority | CharField | Task priority |
| due_date | DateField | Optional deadline |
| created_at | DateTimeField | Creation timestamp |
| updated_at | DateTimeField | Last update timestamp |

#### Design Decisions

- Tasks begin with a pending status.
- Task descriptions are optional.
- Due dates are optional.
- Priority defaults to Medium.
- User ownership will be introduced in Level 3.

### Database Migrations

- Task model defined in `tasks/models.py`.
- Initial migration generated using `makemigrations`.
- Migration operations reviewed before application.
- Migration applied using `migrate`.



- [ ] CRUD functionality

### Level 2 — Task Management Improvements

- [ ] Task search
- [ ] Task filtering
- [ ] Task sorting
- [ ] Priority management
- [ ] Due dates and overdue tracking

### Level 3 — Authentication and User Management

- [ ] User registration
- [ ] Login and logout
- [ ] User-specific tasks
- [ ] Access control

### Level 4 — Advanced Features

- [ ] Notifications and reminders
- [ ] Recurring tasks
- [ ] Calendar view
- [ ] REST API
- [ ] Automated testing
- [ ] Deployment

## Technical Notes

Important concepts, architectural decisions, implementation notes, and lessons learned.

### Environment Configuration

- Environment variables managed with `django-environ`.
- Local secrets stored in `.env`.
- `.env.example` documents required variables.
- Sensitive files excluded through `.gitignore`.
- Production configuration will use hosting-provider environment variables.

## Setup Instructions

Instructions for installing dependencies, configuring the environment, and running the project.

![Project Application Installation Starter 1 ](docs/images/project-installation-1.png)

![Project Application Installation  Starter 2](docs/images/project-installation-starter-2.png)


## Project Tree


todo-list/
│
├── .venv/
│
├── config/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── tasks/
│   ├── migrations/
│   │   └── __init__.py
│   │
│   ├── templates/
│   │   └── tasks/
│   │       ├── base.html
│   │       ├── task_list.html
│   │       ├── task_detail.html
│   │       ├── task_form.html
│   │       └── task_confirm_delete.html
│   │
│   ├── static/
│   │   └── tasks/
│   │       └── css/
│   │           └── style.css
│   │
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   ├── urls.py
│   └── forms.py
│
├── .gitignore
├── db.sqlite3
├── manage.py
├── requirements.txt
└── README.md



Okay understand and implemented, let's proceed  to the next stage on Level 1 why keeping the engineering intact