# django-ng
This is a project ofDjango RESTAPI & Angular

Open 2 command windows

navigate to both folders

/crud/>>ng serve

/djangocrud/>>python manage.py runserver




##ToDo

pip install django-cors-headers

and then add it to your installed apps:

	INSTALLED_APPS = (
	    ...
	    'corsheaders',
	    ...
	)

You will also need to add a middleware class to listen in on responses:

MIDDLEWARE = [  # Or MIDDLEWARE_CLASSES on Django < 1.10
    ...
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    ...
]

allowed hosts========

CORS_ORIGIN_WHITELIST = (
    'google.com',
    'hostname.example.com',
    'localhost:8000',
    '127.0.0.1:9000'
)
