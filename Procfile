web: gunicorn lbg_site.wsgi:application --workers 3
release: python manage.py migrate --noinput && python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'adminpass')"

