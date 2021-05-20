[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg?style=flat-square)](https://github.com/wemake-services/wemake-python-styleguide)

# Django blog

## Installation

Create and activate virtual environment:

```bash
$ virtualenv -p python3 ~/virtualenvs/django-blog
$ source ~/virtualenv/django-blog/bin/activate
```

then install requirements:

```bash
$ pip install -r requirements/dev.txt
```

## Running project

perform migrations:

```bash
$ python manage.py migrate
```

create superuser:

```bash
$ python manage.py createsuperuser
```

start development server:

```bash
$ python manage.py runserver
```

ltog into Django admin panel:

```bash
$ xdg-open http://localhost:8000/admin/
```

## Generate translations

make sure that `locale` directory exists in you root directory and type:

```bash
$ python manage.py makemessages -l pl
$ python manage.py compilemessages
```
