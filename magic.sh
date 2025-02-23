

python manage.py migrate
# python manage.py createsuperuser --noinput --username admin --email admin@example.com
python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin')"