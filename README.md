# Todo-list Application

A fully-featured, production-ready Django Task Management web application built with a custom Bootstrap 5 UI, optimized database queries, and clean code standards.

## Tech Stack

* **Backend**: Python, Django (MVT architecture, Class-Based Views)
* **Frontend**: Bootstrap 5, HTML5, CSS
* **Database**: SQLite

## Features

* **Task Management**: Full CRUD operations for tasks with creation timestamps, deadlines, and completion status toggles.
* **Tag Management**: Full CRUD operations for organizing tasks with custom tags.
* **Performance**: Optimized database queries using `prefetch_related` and `annotate` to eliminate N+1 query bottlenecks.
* **Pagination**: Integrated pagination for smooth navigation (3 tasks per page, 5 tags per page).
* **UI/UX**: Custom Bootstrap 5 design with clear status indicators and responsive sidebar navigation.

## Getting Started

### Prerequisites

* Python 3.10+
* pip

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd Todo-list
Create and activate a virtual environment:

Bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
Install dependencies:

Bash
pip install -r requirements.txt
Apply database migrations:

Bash
python manage.py migrate
Run the development server:

Bash
python manage.py runserver
Open your browser and navigate to http://127.0.0.1:8000/.