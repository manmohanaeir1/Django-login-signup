# Django Login and Signup Project

This project is a simple Django-based web application that implements a login and signup system. It includes user authentication, logout functionality, and a styled user interface for the login form.

---

## Features

- **User Authentication**: Users can log in and log out securely.
- **Signup Functionality**: New users can create accounts.
- **CSRF Protection**: Ensures secure form submissions using Django's built-in CSRF token.
- **Customizable Templates**: Uses Django's templating system for reusable and extendable HTML templates.
- **Static File Management**: Includes CSS for styling the login and logout forms.
- **Redirects**: After login or logout, users are redirected to the appropriate pages.

---

## What I Learned

### 1. **Django Templating System**
   - How to use `base.html` as a reusable layout for other templates.
   - Using `{% block content %}` to inject specific content into child templates.
   - Loading static files with `{% load static %}` and referencing them using `{% static 'path/to/file' %}`.

### 2. **User Authentication**
   - Implementing Django's built-in `LoginView` and `LogoutView`.
   - Securing logout functionality by using `POST` requests with CSRF tokens.
   - Redirecting users after login/logout using `LOGIN_REDIRECT_URL` and `LOGOUT_REDIRECT_URL` in `settings.py`.

### 3. **Static Files**
   - Configuring `STATIC_URL` and `STATICFILES_DIRS` in `settings.py` to serve CSS and other static assets.
   - Linking external CSS files to style the login and logout forms.

### 4. **Form Handling**
   - Creating forms for login and logout using Django's form handling system.
   - Adding CSRF protection to forms with `{% csrf_token %}`.

### 5. **Styling with CSS**
   - Designing a modern and responsive login form with CSS.
   - Adding hover and focus effects to buttons and input fields for better user experience.

---

## Project Structure
