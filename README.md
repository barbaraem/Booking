# Booking
Simple appointment application.



<h2>Requirements</h2>


  Python 3.5+
  Django 1.11 - Base web framework

  dateparser==0.7.0
  decorator==4.1.2
  django-bootstrap-datepicker==1.2.3
  django-bootstrap-form==3.4
  django-cors-headers==2.1.0
  django-extensions==1.9.6
  django-filter==1.1.0
  djangorestframework==3.7.1
  Jinja2==2.10
  pendulum==2.0.1
  psycopg2==2.7.4
  python-dateutil==2.6.1
  pytz==2017.2
  pytzdata==2018.4
  redis==2.10.6
  regex==2018.2.21
  requests==2.18.4
  text-unidecode==1.1
  twilio==6.12.0
  tzlocal==1.5.1
  urllib3==1.22
  uWSGI==2.0.17
  Werkzeug==0.14.1


<h3>Usage</h3>


    Clone or download the repo.
    Create virtualenv.
    Use pip install -r requirements.txt to install requirements in requirements.txt.
    Create a .env file from the example.env file in source directory of the project.
    Edit your .env file to include your own environment values for secret keys, database urls, etc.
    Run python manage.py migrate to run all database migrations.
    Run python manage.py createsuperuser to create an admin user.
    Run python manage.py runserver --no input for a development environment, or use the Django documentation to set up a WSGI-compliant webserver of your choice.

