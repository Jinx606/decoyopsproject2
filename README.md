# DecoyOpsProject2 - Django Project README

Welcome to **DecoyOpsProject2**, a Django project. This README provides essential information on how to set up and run the project locally using virtual environments (venv) and Docker.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Cloning the Repository](#cloning-the-repository)
  - [Virtual Environment Setup](#virtual-environment-setup)
  - [Database Configuration](#database-configuration)
  - [Applying Migrations](#applying-migrations)
  - [Create a Superuser](#create-a-superuser)
  - [Run the Development Server](#run-the-development-server)
- [Using Docker](#using-docker)
  - [Build the Docker Image](#build-the-docker-image)
  - [Run the Docker Container](#run-the-docker-container)
- [Handling Secrets](#handling-secrets)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

### Prerequisites

Before you begin, ensure you have met the following requirements:

- [Python](https://www.python.org/) (3.x recommended)
- [Django](https://www.djangoproject.com/download/) (latest version)
- [Docker](https://www.docker.com/get-started) (if using Docker)

### Cloning the Repository

To get started, clone this repository to your local machine:

- [git clone](https://github.com/jinx606/decoyopsproject2.git)
- cd decoyopsproject2

### Virtual Environment Setup

Create and activate a virtual environment:

- python -m venv venv
- source venv/bin/activate 

Install project dependencies:

- pip install -r requirements.txt

### Database Configuration

Configure your Django application settings in the settings.py file, including database settings, secret keys, and any environment variables.

### Applying Migrations

Apply database migrations to set up the database schema:

- python manage.py migrate

### Create a Superuser

Create a superuser account for administrative access:

- python manage.py createsuperuser

### Run the Development Server

Start the development server:

- python manage.py runserver

You can now access your Django application in a web browser at http://localhost:8000.

### Using Docker

If you prefer to run the application using Docker, follow these steps:

#### Build the Docker Image

Install Docker on your machine (if not already installed).
Build the Docker image:

- docker build -t decoyopsproject2 .

### Run the Docker Container

Start a Docker container based on the image:

- docker run -p 8000:8000 decoyopsproject2

You can access your Django application in a web browser at http://localhost:8000.

### Handling Secrets

Important: Sensitive information like passwords and access tokens should never be committed to public repositories. To configure your Django project with these secrets, follow these steps:

1. Create a .env file in the root directory of your project:

: # .env
: SECRET_KEY=mysecretkey
: DATABASE_URL=your-database-url
: DEBUG=True  # Set to False in production

2. In your Django settings.py file, load environment variables from the .env file:

: import os
: from dotenv import load_dotenv

: load_dotenv()

: SECRET_KEY = os.environ.get('SECRET_KEY')
: DATABASE_URL = os.environ.get('DATABASE_URL')
: DEBUG = os.environ.get('DEBUG') == 'True'

Replace mysecretkey and your-database-url with your actual secrets.

By following these steps, you can keep your secrets secure and separate from your codebase.

### Contributing

Contributions are welcome! If you'd like to contribute to this project, please fork the repository, make your changes, and submit a pull request.

### License

This project is licensed under the MIT License.

### Note:

Please make sure that you have a `requirements.txt` file in your project's root directory containing the dependencies required to run your Django application.