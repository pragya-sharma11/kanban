# Kanban Application

## Structure

- /src - react code
- /relevvo - django app

## To Setup Backend

- You need to have Python 3 at least installed.

```sh
$ git clone URL
$ cd web-application
$ pip install pipenv
$ python -m pipenv shell
$ pip install -r requirements.txt
$ python manage.py migrate
$ python manage.py createsuperuser
$ python manage.py runserver
```

## To Setup Backend

```sh
$ npm install
$ npm start
```

Now you can go to:

- http://localhost:3000 for frontend
- http://localhost:8000/api/ for Django REST API (see local environment in postman)
- http://localhost:8000/admin/ for the Django admin
