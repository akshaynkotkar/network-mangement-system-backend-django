Project Setup
Clone Project: git clone https://github.com/akshaynkotkar/network-mangement-system-backend-django.git

Create Virtual Environment 
cmd-> python3 -m venv venv
Activate Virtual ENV
cmd-> source venv/bin/activate

Now Install required packages
cmd-> pip install -r requirements.txt
Migration commands
cmd->1)python manage.py makemigrations categories
     2)python manage.py makemigrations locations
     3)python manage.py migrate

Then Run Project using
cmd-> python manage.py runserver

