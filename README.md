Setup project environment with virtualenv and pip.

$ virtualenv project-env
$ source project-env/bin/activate
$ pip install -r requirements.txt
$ python manage.py runserver


Url:

    http://127.0.0.1:8000/data/<type>

    type can be "users", "products"