Plank
============

Plank is a status board for websites, services and APIs, like Amazon's `AWS status page`_.

It is heavily based on my `whiskerboard fork`_. 

I'm not following the current strategy of the origina repo, so I decided to rename my fork
and have it available under a different name as to not confuse whiskerboard users.


Quick start guide
-----------------

    $ git clone git@github.com:sijis/django-plank.git
    $ cd django-plank
    $ sudo pip install -r requirements.txt
    $ Add a "SECRET_KEY = 'EnterABunchOfRandomCharactersHere'" to settings/base.py
        (Alternatively, use http://www.miniwebtool.com/django-secret-key-generator/ to create a secret key!)
    $ ./manage.py syncdb
    $ ./manage.py migrate
    $ ./manage.py runserver

Back on the admin home page, click on "services" and add the things you want to report the status of (website, API etc).
To change the status of a service add an event via the admin pages or use the api.

API Documentation
-----------------

For now, visit the `whiskerboard wiki`_ for details about the API.

You may also find useful the `whiskerboard-tools repository`_.

.. _AWS status page: http://status.aws.amazon.com/
.. _whiskerboard fork: http://github.com/sijis/whiskerboard
.. _whiskerboard wiki: http://github.com/sijis/whiskerboard/wiki
.. _whiskerboard-tools repository: http://github.com/sijis/whiskerboard-tools
