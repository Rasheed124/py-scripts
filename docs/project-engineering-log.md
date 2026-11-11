# TaskFlow — Project Engineering Log

**Project:** TaskFlow
**Repository:** `Rasheed124/py-scripts`
**Production Branch:** `todo-list`
**Documentation Branch:** `docs/update-project-engineering-log`
**Current Engineering Level:** Level 4
**Last Updated:** 11 November 2026

---

## 1. Engineering Overview

TaskFlow is a Django-based task management application developed to demonstrate practical software engineering principles, including application architecture, database management, authentication, automated testing, production deployment, and continuous integration.

The project follows an incremental engineering approach. Each development stage introduces specific concepts, implementation decisions, and verification procedures.

The objective is to maintain a reliable, maintainable application while progressively introducing production-level engineering practices.

## 2. Application Architecture

The application follows Django's project-and-app architecture.

### Main Components

| Component | Responsibility |
|---|---|
| `config/` | Project configuration, settings and application entry points |
| `accounts/` | User authentication and account-related functionality |
| `tasks/` | Task and category management |
| `docs/` | Engineering documentation and project resources |
| `.github/workflows/` | GitHub Actions automation |
| `manage.py` | Django management commands |

### Configuration Structure

The settings configuration is separated by environment:

config/
├── settings/
│   ├── __init__.py
│   ├── base.py
│   ├── development.py
│   └── production.py
├── __init__.py
├── asgi.py
├── urls.py
└── wsgi.py


This separation keeps shared application configuration independent from environment-specific settings.

### Technology Stack

- Python
- Django
- SQLite for local development
- PostgreSQL for production
- Gunicorn
- WhiteNoise
- django-environ
- Git and GitHub
- GitHub Actions
- Render

## 3. Engineering Progress

### Level 1 — Python and Django Fundamentals

**Status:** Completed

Established the Python and Django fundamentals required to develop the application.

Key learning areas included Python programming, Django project structure, models, views, URLs, templates, static files, the Django admin interface, and database migrations.

### Level 2 — Core Application Development

**Status:** Completed

Implemented the foundational TaskFlow functionality.

Major components include:

- Task and category models.
- Task creation, retrieval, updating and deletion.
- Category management.
- Django authentication integration.
- User-specific task and category ownership.

### Level 3 — Application Enhancement and Testing

**Status:** Completed

Expanded the application with additional functionality and automated verification.

Implemented areas include:

- Task search and filtering.
- Sorting and pagination.
- Dashboard statistics.
- Authentication and authorization checks.
- Organized automated tests.

**Verification:** 84 automated tests passed.

### Level 4 — Production Engineering and Deployment

**Status:** In Progress

The focus of this level is production readiness, deployment, CI/CD, advanced application functionality, and ongoing maintenance.

#### Phase 4.1 — Production Readiness

**Status:** Completed

Implemented production-oriented configuration.

Key activities:

- Separated development and production settings.
- Configured environment variables and secrets.
- Introduced PostgreSQL configuration.
- Configured Gunicorn.
- Integrated WhiteNoise for static file delivery.
- Configured production static-file storage.
- Reviewed production security settings.
- Configured production logging.
- Prepared deployment configuration.

#### Phase 4.2 — Initial Deployment

**Status:** Completed

Successfully deployed TaskFlow to Render.

Deployment activities:

- Configured the production database.
- Configured the Render web service.
- Installed production dependencies.
- Collected static files during the build.
- Applied database migrations.
- Started the application using Gunicorn.
- Verified that the deployed application operates successfully.

**Production platform:** Render

#### Phase 4.3 — Continuous Integration (CI)

**Status:** Implemented — Pull-request workflow validation ongoing.

GitHub Actions has been introduced to automate application quality checks.

The workflow currently covers:

- Python environment setup.
- Dependency installation.
- Django system checks.
- Migration consistency checks.
- Automated test execution.

**Local verification:**

| Check | Result |
|---|---|
| `python manage.py check` | Passed |
| `python manage.py makemigrations --check --dry-run` | Passed |
| `python manage.py test` | 84 tests passed |

**GitHub Actions verification:**

The initial GitHub Actions workflow completed successfully. All configured quality-check steps passed.

#### Phase 4.4 — Continuous Deployment (CD)

**Status:** Pending

Planned activities:

- Connect successful CI checks to controlled production deployment.
- Configure deployment secrets securely.
- Automate deployment verification.
- Review migration execution during deployment.
- Establish rollback procedures.
- Introduce release and versioning practices.

#### Phase 4.5 — Advanced Application Features

**Status:** Pending

Planned functionality:

- Reminders and email notifications.
- Recurring tasks.
- Calendar view.
- Bulk task operations.
- CSV export.
- REST API using Django REST Framework.
- Expanded integration and regression tests.

#### Phase 4.6 — Production Monitoring and Maintenance

**Status:** Pending

Planned activities:

- Application logging and error monitoring.
- Database backup and recovery.
- Performance monitoring.
- Dependency maintenance.
- Security reviews.
- Production troubleshooting.

---

## 4. Development and Collaboration Workflow

The project uses Git branches to separate production code from ongoing development.

### Main Branches

| Branch | Purpose |
|---|---|
| `main` | Repository overview and broader learning structure |
| `django` | Django learning work |
| `todo-list` | TaskFlow application and production branch |
| Feature/documentation branches | Isolated changes before integration |

### Integration Workflow

The intended integration process is:

1. Create a dedicated feature or documentation branch from `todo-list`.
2. Implement and test the changes.
3. Commit and push the branch.
4. Open a pull request targeting `todo-list`.
5. Allow GitHub Actions to execute the required quality checks.
6. Review the changes.
7. Merge after the required checks pass.

The `todo-list` branch has a GitHub branch protection rule configured to support controlled integration through pull requests.

Required status-check selection and pull-request enforcement will be verified as part of the CI integration process.

---

## 5. Engineering Principles

The following principles guide further development:

- Keep application responsibilities separated.
- Avoid unnecessary abstractions.
- Use environment variables for environment-specific configuration.
- Never commit production secrets.
- Preserve backward compatibility where practical.
- Use database migrations to manage schema changes.
- Write automated tests for application behaviour.
- Run quality checks before integrating changes.
- Keep production configuration separate from development configuration.
- Document significant architectural decisions.

---

## 6. Current Engineering Priorities

The immediate priorities are:

1. Complete CI integration with the protected `todo-list` branch.
2. Verify pull-request status checks and branch protection behaviour.
3. Finalize the engineering documentation.
4. Proceed to Phase 4.4 — Continuous Deployment.

**Current milestone:** Establishing a reliable pull-request and continuous-integration workflow before automating production deployments.
