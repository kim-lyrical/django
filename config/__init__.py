'''
python -m venv venv
source venv/bin/activate
which pip
pip install django
pip install pillow
pip install djangorestframework
pip install django-rest-swagger==2.1.2

django-admin startproject config .


python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser
python manage.py startapp packets

python manage.py runserver


'''