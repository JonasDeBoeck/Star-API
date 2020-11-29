release: python manage.py makemigrations --no-input
release: python manage.py migrate --no-input

web: gunicorn Ster_API.wsgi --log-file -