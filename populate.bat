@echo off
python manage.py makemigrations computingcomms
python manage.py migrate
python populate_computingcomms.py