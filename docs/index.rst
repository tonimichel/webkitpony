###############################################################
Welcome to webkitpony's documentation!
###############################################################

    “build webapp-like desktop applications”
    
    

    
    
webkitpony is a micro framework to build dektop applications with web technologies on the basis of
the python binding of the webkit rendering engine (http://code.google.com/p/pywebkitgtk/).

.. image:: img/pony.png
    :align: center

Artwork by `IYOMI <http://iyomi.de>`_\

*********************
Motivation
*********************

Building desktop applications with standard toolkits like GTK works fine - but tweaking the UI 
beyond the boundaries of window managers is exhausting. In contrast, building a web ui with HTML, 
Javascript and CSS is quite flexible. Acctually, the motivation behind webkitpony was to stay in a
djangonaut-familiar environment when it comes to build desktop applications. As the basic technology  
(the webkit rendering engine) was given - it was about playing around and creating a simple-to-use django-like
development process. The result was webkitpony.

At `schnapptack <http://schnapptack.de>`_\, we use this approach for building desktop applications or solutions that
explicitely need a non-browser client. Often we also combine having native logic and remote logic from a web application.

*********************
Goal
*********************

The goal of webkitpony is to provide an alternative to standard desktop application development approaches.
It especially targets on developers familiar with django. However, the framework is so simple, that even non-django
programmers will get the point fastly.


******************************************
Understanding webkitpony
******************************************

.. toctree::
    :maxdepth: 3

    understanding
    webview_class
    webkitpony_js
    settings
    
    
*********************
Getting started
*********************

.. toctree::
    :maxdepth: 3
    
    install
    tutorial
    
    
*********************
Indices and tables
*********************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

