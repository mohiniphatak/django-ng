pip install django-cors-headers(already installed-install if ur using new machine)

and then add it to your installed apps:(already added)

	INSTALLED_APPS = (
	    ...
	    'corsheaders',
	    ...
	)

You will also need to add a middleware class to listen in on responses:(already added)

MIDDLEWARE = [  # Or MIDDLEWARE_CLASSES on Django < 1.10
    ...
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    ...
]

allowed hosts========(already added)

CORS_ORIGIN_WHITELIST = (
    'google.com',
    'hostname.example.com',
    'localhost:8000',
    '127.0.0.1:9000'
)