# Task Manager – CS50 Final Project

#### Video Demo:  <https://drive.google.com/file/d/1vcFnMJb2xn_lvoqa7D-kUV3zFqG4f6yT/view?usp=sharing>

## Overview

Task Manager is a web-based to-do list application built with Python’s Flask framework and SQLite for data storage. The primary goal of this project is to provide users with a simple and intuitive interface to create, manage, and complete tasks in an organized way, while ensuring that all tasks are private and tied to individual user accounts.

The application supports user registration, login, and logout functionality, ensuring that each user’s data is secure and accessible only to them. Once logged in, users can add new tasks, mark tasks as completed (which visually strikes them through), and delete tasks they no longer need.

This project was developed as part of my CS50x Final Project, demonstrating my understanding of Flask routing, database integration, user authentication, and HTML/CSS/Bootstrap for frontend design.

---

## Features

1. **User Authentication**
   - **Register**: Users can create an account with a unique username and secure password.
   - **Login**: Existing users can log in to access their personal task list.
   - **Logout**: Users can log out, which clears their session and prevents unauthorized access.
   - Passwords are stored securely using Werkzeug’s password hashing functionality.

2. **Task Management**
   - **Add Tasks**: Users can create new tasks using a simple input form.
   - **Mark Complete**: Clicking a “Complete” button marks a task as completed and applies a strikethrough style in the task list.
   - **Delete Tasks**: Tasks can be permanently deleted from the database with a single click.

3. **Session Management**
   - Flask sessions ensure users stay logged in across requests until they log out.
   - Routes are protected with a custom `@login_required` decorator to prevent unauthorized access.

4. **Database**
   - SQLite is used as the storage engine.
   - The `users` table stores user credentials.
   - The `tasks` table stores all tasks along with the `user_id` to link tasks to their owner.

---

## File Structure

### **app.py**
This is the main application file where:
- Routes for registration (`/register`), login (`/login`), logout (`/logout`), homepage (`/`), add (`/add`), complete (`/complete/<id>`), and delete (`/delete/<id>`) are defined.
- Session configuration is handled.
- Database queries for inserting, selecting, updating, and deleting tasks are executed.
- Input validation is performed at both HTML form level (`required` attribute) and Python backend level.

### **helpers.py**
Contains helper functions, including:
- `apology(message, code)`: Renders an error message page when an issue occurs (e.g., invalid login).
- `login_required(f)`: A decorator that ensures certain routes can only be accessed when the user is logged in.

### **templates/layout.html**
The base HTML layout for all pages. Contains:
- Bootstrap integration for styling.
- A navigation bar that adapts based on whether the user is logged in or not.
- A `{% block main %}` section for injecting page-specific content.

### **templates/register.html**
A registration form with fields for username, password, and password confirmation. Includes validation to ensure passwords match.

### **templates/login.html**
A login form that accepts a username and password and validates them against the database.

### **templates/index.html**
Displays the logged-in user’s tasks in a table format. Each row has:
- The task name.
- A “Complete” button to mark the task as finished.
- A “Delete” button to remove the task.

### **static/styles.css**
Contains any custom CSS overrides to style the application beyond Bootstrap’s defaults, including the strikethrough style for completed tasks.

---

## Database Structure

**users table**
- `id` (INTEGER PRIMARY KEY)
- `username` (TEXT, unique)
- `hash` (TEXT, storing the password hash)

**tasks table**
- `id` (INTEGER PRIMARY KEY)
- `user_id` (INTEGER, foreign key referencing users.id)
- `task` (TEXT, the task description)
- `completed` (INTEGER, 0 for incomplete, 1 for completed)

---

## Design Decisions

### **Why Flask?**
Flask was chosen for its simplicity, flexibility, and suitability for small-to-medium web projects. It allowed me to focus on implementing core logic without dealing with the overhead of a large framework.

### **Why SQLite?**
SQLite is a lightweight relational database that integrates perfectly with Flask for small projects. It requires no additional server configuration, making deployment and testing easier.

### **Password Hashing**
Instead of storing plain text passwords, I used Werkzeug’s `generate_password_hash` and `check_password_hash` functions. This decision was made to align with best practices in web security.

### **Task Completion UI**
When a task is completed, the database updates its `completed` field. The frontend checks this field and applies a CSS class to strike through the task. This gives immediate visual feedback without cluttering the UI.

### **HTML Validation vs Backend Validation**
Even though HTML5 `required` attributes handle some validation, all critical checks are repeated in the backend to prevent users from bypassing them with manual HTTP requests.

---

## How to Run the Project

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
