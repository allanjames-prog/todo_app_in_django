# To-Do List Application

## Overview

This is a simple and interactive To-Do List web application built with Django and Bootstrap. The application allows users to create tasks, set due dates, assign priorities, and mark tasks as complete. It features a dark mode UI for a better user experience and uses AJAX to update the task status in real-time without requiring a page refresh.

## Features

- **Add Tasks**: Users can add tasks with a name, description, due date, and priority level.
- **Mark Tasks as Complete**: Tasks can be marked as complete with a single click, and the status is updated dynamically without reloading the page.
- **Dark Mode**: The application has a modern dark mode design, enhancing usability during low-light conditions.
- **Task List**: A dynamic list of tasks is displayed, and the status of each task (completed or not) is visible.
- **Priority Levels**: Each task can be assigned a priority (High, Medium, or Low).
- **Real-Time Updates**: Task completion status updates live using AJAX and Django's backend.

## Technologies Used

- **Django**: The backend framework used for handling requests and serving data.
- **Bootstrap**: The frontend framework for responsive design and styling.
- **AJAX**: Used for asynchronous communication between the client and server, enabling real-time updates of task statuses.
- **Python**: The programming language used for backend development with Django.
- **HTML, CSS**: Markup and styling for the frontend.

## Installation

To run this project locally, follow these steps:

### Prerequisites
Make sure you have the following installed:
- Python 3.x
- Django 3.x or higher

### Clone the repository

```bash
git clone <repository_url>
cd <project_directory>
```

### Install dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

### Set up the database

Make sure to apply the migrations to set up the database schema:

```bash
python manage.py migrate
```

### Run the development server

Start the Django development server:

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser to access the To-Do List application.

## Usage

1. **Adding Tasks**: Use the form at the top to add new tasks, providing a task name, description, due date, and priority.
2. **Marking Tasks Complete**: After adding tasks, you can mark them as complete by clicking the "Mark as Complete" button next to the task.
3. **Live Updates**: The task status will change to "Completed" and the button will be disabled immediately after marking a task as complete.

## Folder Structure

```
/todo_list
    /migrations
    /static
        /css
        /js
    /templates
        /todo_list
            - home.html
    /models.py
    /views.py
    /urls.py
    /forms.py
    /admin.py
    /tests.py
    /settings.py
    /requirements.txt
```

- **`models.py`**: Contains the `TodoList` model for the tasks.
- **`views.py`**: Handles the logic for rendering the task list and updating the task status.
- **`urls.py`**: Defines the routes for the application.
- **`home.html`**: The template for the main page that displays the tasks and handles form submissions.

## Contributing

If you'd like to contribute to this project, please fork the repository, create a new branch, make your changes, and submit a pull request.

## License

This project is open source and available under the MIT License.
