django-restangular
==================

Example project using Django and AngularJS. AngularJS static files are served through Django static files for commodity (to avoid CORS mechanisms).

Installation
------------
1.  Create your virtualenv and install requirements :

        virtualenv virtenv
        source virtenv/bin/activate
        pip install -r requirements.txt

2.  Run development server :
        
        python manage.py syncdb
        python manage.py runserver

    If you change the server port, you will also have to edit the port in the `services.js` file.

3.  Go to `http://localhost:8000`
