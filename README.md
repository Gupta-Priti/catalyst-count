# Catalyst Count Web Application

## Overview
This is a Django-based web application that allows users to upload large CSV files, visualize the upload progress, store the data in a PostgreSQL database, and perform data filtering based on user-defined criteria. The application also includes user authentication, secure environment variable handling, and a Bootstrap-based user interface.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Features](#features)
- [Dependencies](#dependencies)


## Installation

1. Clone the repository:

git clone https://github.com/Gupta-Priti/catalyst-count.git


2. Navigate to the project directory:
cd catalyst-count


3. Install dependencies:
pip install -r requirements.txt


4. Set up environment variables:
- Create a `.env` file in the project root directory.
- Define the required environment variables in the `.env` file (e.g., database credentials, secret keys).
- Make sure to keep the `.env` file private and never share it publicly or include it in version control. Add `.env` to your `.gitignore` file to ensure it's not accidentally committed to your repository.

Before running the application, ensure you have set up the following environment variables:

a. **DEBUG:** Set to `True` for development and debugging purposes.
b. **SECRET_KEY:** Generate a new Django secret key and replace `'your_secret_key_here'` with it.
c. **DATABASE_URL:** Provide the PostgreSQL database URL in the following format:

postgres://username:password@host:port/database_name


5. Create the media folder in the project root directory if it doesn't already exist:
mkdir media

Inside the media folder, create an uploads folder to store uploaded files:
mkdir media/uploads


6. Apply database migrations:
python manage.py migrate


7. Create a superuser by running:
python manage.py createsuperuser
Follow the prompts to enter the desired username, email, and password for the superuser.


8. Run the development server:
python manage.py runserver


9. Access the application at `http://127.0.0.1:8000/` in your web browser.


## Usage

1. **Login:** Users can log in to access the application features.
2. **Upload Data:** Allows users to upload a large CSV file with a visual progress indicator.
3. **Query Builder:** Users can perform queries to filter the uploaded data.
4. **Users:** Admin interface to manage users.


## Project Structure

- `catalyst-count/`: Django project directory containing settings, URLs, and WSGI configurations.
- `media/uploads/`: Directory to store uploaded CSV files.
- `templates/`: Contains HTML templates for the user interface.
- `users/`: Django app for user management, including models, views, forms, and URLs.


## Features

- User authentication and authorization using django-all-auth.
- Secure handling of environment variables using django-environ.
- Progress bar for visual upload indication.
- PostgreSQL database integration for data storage.
- Build and submit queries using a form to filter data.
- Display the count of records based on applied filters.
- Admin interface to manage users.
- Logout functionality to end the user's session.
- Bootstrap 4 for responsive and modern UI design.
- Unit testing for server-side functionalities.


## Dependencies

- Django 3.x/4.x
- PostgreSQL
- django-environ
- django-all-auth
- Bootstrap 4/5

Refer to `requirements.txt` for a detailed list of dependencies and versions.

