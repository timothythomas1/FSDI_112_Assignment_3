# FSDI_112_Assignment_3

## Project set up 

### Instructions

1. Create a virtual environment.
2. Activate venv.
3. Install django.
4. Create new djagno project using "config" as the name for the directory and containing folder as ourproject directory. 
5. Create an app called "posts".
6. Run our default migrations.
7. Create an administrator user (super user).
8. Run our server and ensure we can see the rocket ship template.

# Create a virtual environment
❯ python3 -m venv venv
❯ source venv/bin/activate
❯ pip3 install django

# Check Django Commands
❯ django-admin

# (Creates a config dir and manage.py file)
❯ django-admin startproject config . 
❯ python3 manage.py

# (Creating a new "app")
❯ python3 manage.py startapp <name>
❯ python3 manage.py migrate

# (Creating a new user)
❯ python3 manage.py createsuperuser

# (Run the server)
❯ python3 manage.py runserver

# (Open in VS Code)
❯ python3 manage.py startapp pages
❯ code .

After running server, you can go to /admin to log in.;

(GitHub Open Sourced Repo)
https://github.com/django/django