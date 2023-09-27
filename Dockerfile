# Use an official PyPy runtime as a parent image
FROM pypy:latest

# Set environment variables for Python
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE myproject.settings

# Create and set the working directory
RUN mkdir /app
WORKDIR /app

# Copy the Pipfile and Pipfile.lock for Python dependency installation
COPY Pipfile Pipfile.lock /app/

# Install system dependencies
RUN apt-get update && apt-get install -y \
    # Add any system dependencies your app needs here \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies using Pipenv
RUN pip install pipenv
RUN pipenv install --deploy --ignore-pipfile

# Copy the Django project files into the container
COPY . /app/

# Expose the port your application will run on
EXPOSE 8000

# Run Django's development server
CMD ["pipenv", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
