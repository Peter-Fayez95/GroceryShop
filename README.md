# Grocery Shop Website

A Django-based web application that lists Egyptian products scraped from Amazon and Carrefour.

## Introduction

This project is a web application built with Django that showcases a variety of Egyptian grocery products. The products are scraped from major retailers like Amazon and Carrefour, providing an extensive list for users to browse.

## Features

- Lists Egyptian grocery products scraped from Amazon and Carrefour
- User-friendly interface for browsing and searching products
- Built with Django, ensuring a robust and scalable backend

## Prerequisites

Before you begin, ensure you have met the following requirements:

- **Python 3.6+** installed on your machine
- **Git** installed for cloning the repository
- **PostgreSQL** database (hosted on [Neon.tech](https://neon.tech/) or any other PostgreSQL provider)
  - Acquire your database credentials (hostname, database name, username, password, and port)

## Installation

Follow these steps to set up the project locally:

### 1. Clone the Repository

Open your terminal and run:

```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
```

### 2. Create a Virtual Environment
Create a virtual environment to manage dependencies:

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment
- On Windows:

```bash
venv\Scripts\activate
```

- On macOS/Linux:
```bash
source venv/bin/activate
```

### 4. Install Dependencies
Install the required Python packages using `pip`:

```bash
pip install -r requirements.txt
```

## Configurations
Create a .env file in the root directory of the project to store environment variables:
```bash
touch .env
```
Populate the .env file with the following variables:

```bash
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3
```

- `SECRET_KEY`: A secret key for Django security purposes. You can generate one using tools like Django Secret Key Generator.
- `DEBUG`: Set to True for development. In production, set it to False.
- `ALLOWED_HOSTS`: A comma-separated list of hosts/domain names that the Django site can serve.
- `DATABASE_URL`: Your PostgreSQL database URL. Replace username, password, hostname, port, and database_name with your actual credentials from Neon.tech.

## Database Migrations
Apply migrations to set up the database schema:

```bash
python manage.py makemigrations
python manage.py migrate
```

## Populating the Database
Populate the database with scraped products:
```bash
python manage.py runscript data
```

- Ensure that the data script is properly set up to scrape data from Amazon and Carrefour.
- This script will fetch the latest products and store them in your database.

## Running the Application
Start the Django development server:

```bash
python manage.py runserver
```
The application will be available at http://127.0.0.1:8000/.

