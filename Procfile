
web: gunicorn taskproject.wsgi --log-file - 
#or works good with external database
web: python manage.py migrate && gunicorn taskproject.wsgi
