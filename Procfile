release: python manage.py makemigrations; python manage.py migrate --noinput; python manage.py compress --force
web: gunicorn config.wsgi:application
worker: celery worker --app=config.celery_app --loglevel=info
beat: celery beat --app=config.celery_app --loglevel=info
