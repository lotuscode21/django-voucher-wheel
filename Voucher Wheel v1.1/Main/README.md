# Voucher Wheel
A dashboard for manager information using [Django](https://www.djangoproject.com/).

## Run Docker
First you need to create the `.env` file. You can do that, using the example:

    cp .env.example .env

Then, you can start the container:

    docker-compose up [-d]
    
To update the database:

    $ docker exec -it ice-comms_fruit_machine sh
    /fruit_machine # python manage.py migrate

### Create admin user

    /fruit_machine # python manage.py createsuperuser
    Username (leave blank to use 'user'): admin
    Email address: admin@localhost
    Password:
    Password (again):
    Superuser created successfully.

### Create the static files

    /fruit_machine # python manage.py collectstatic
    179 static files copied to '/fruit_machine/static'.

### Load the initial data

    /fruit_machine # python manage.py loaddata prizes
    Installed 15 object(s) from 1 fixture(s)

## Prepare a local (_host_) environment
Create the local python environment:

    $ virtualenv venv --python=python3
    $ source venv/bin/activate
    $ pip install -r fruit_machine/requirements.txt
