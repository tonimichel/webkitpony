webkitpony
=========================

building webapp-like desktop apps in python

License: MIT

.. image:: http://schnapptack.de/media/webkitpony.jpg

Artwork by IYOMI

What webkitpony is about
==========================

webkitpony is a micro framework to build desktop applications with web technologies.
Its a lightweight piece of code sitting on top of the webkit rendering engine enabling 
a django-like development process for desktop applications.
Take a look at the demo project "ponyhof". The structure will look familiar to all djangonauts.


Motivation
==============================

Building desktop applications with standard toolkits like GTK works fine - but tweaking the UI 
beyond the boundares of window managers is exhausting. In contrast building a web ui with HTML, 
Javascript and CSS quite flexible. 


Documentation
=======================

Project structure
----------------------------

webkitpony gives a django-inspired structure to your project. The following figure shows
the example project _ponyhof_:

..img 'project_structure.png'

As you can see, the structure is quite similar to the one of a django project.
We have a urls.py, a views.py, a templates dir and a static dir. 


The principle
----------------------------------

To understand webkitpony,
it is important to understand the communication between web ui and python code:

..img 'sss'


The web ui is the webkit webview. Every time a link is clicked, the url of that link, namely the href
attribute is sent to the webkitpony url dispatcher, which looks up the url patterns
and triggers the view, passing the webview and the passed url parameters. 


A basic example
-------------------------------

:: 

    <body>
        <a id="calculate" href="/calculate/27/">Calculate</a>
    </body>


::
 
    urlpatterns = (
        (r'^calculate/<>/', views.calculate)
    )
    

::

    def calculate(webview, id):
        # do some stuff
        return webview.render('myapplication/myview.html', {
            'this': 'is',
            'the': 'template context'
        })
})


So, the principle is quite familiar to django urls and views. A url is defined of a 
regex and a callback function (the view) to be executed.
In fact the only difference is, that our view takes a webview object (instead of request) and returns
webview.render (instead of a HttpResponse). The webview.render renders a template applying the
passed context.

Passing data from HTML to Python
------------------------------------------------------

Sometimes we want to build our UI completely in Javascript, or at least send some form data
to our application. So, we need a way to pass data from html to the application. As we
are not in the web, we do not have POST or GET. To solve this issue, webkitpony provides 
a Javascript connector enabling an Ajax-like JSON communicaton between javascript and python code.
Consider the following example:

::
 
    # html
    <body>
        
        <a id="calculate" >Calculate</a>
        
        <script>
            a.click(function() {
                webkitpony.send('/calculate/', {data: data}, function(response) {
                    console.log('We sent ' + data + ' and received ' + response)
                })
            })
        </script>
    </body>
    
::

    # urls.py
    
    urlpatterns = (
        (r'^calculate/$', views.calculate)
    )
    
::
 
    # views.py
    
    def calculate(webview):
        result = backend.perform_calculation(webview.data)
        return webview.json_response({'result': result})        
        
        
Lets start at the UI. The HTML defines a button 'Calculate'. Whenever this button is clicked, 
webkitpony.send(url, data, callback) is invoked. This method is comparable with an
ajax request with the difference that, instead of a Http request, the url dispatcher is triggered
passing '/calculate/27/'.
So, once clicked, url and data are passed
to the python side, where the urlpatterns match the url and invoke the view function.
The view function unpacks the data from webview (similiarily to request.POST),
performs the calculation and returns a webview.json_response(json_serializable_data). In
contrast to webview.render, the webview is not re-rendered. Instead json is passed back
back to webkitpony.send which finally executes ts callback function.


The webview class
----------------------------------

Every view function takes a webview object as first parameter. In fact the webview object is
the embedded browser itself and provides two methods to talk back to the UI:

webview.render(template, context)
Renders template applying context directly to the webview.

webview.json_response(data)
Takes a json-serializable data structure and triggers the callback mechanism from webkitpony.send


webkitpony.js
-----------------------------------

Provides one single method webkitpony.send(url, data, callback) and enables an ajax-like
communication with the python side. <data> is json-serializable Javascript object. callback
is triggered when the python side has finished the "request".



Settings
----------------------------------

:: 

    WIDTH = 1000

    HEIGHT = 1000

    INSPECTOR = True

    RESIZABLE = True




Installation and requirements
=============================================================

Before you install webkitpony, make sure you have the following libraries and tools installed:

* pywebkitgtk (http://code.google.com/p/pywebkitgtk/)
* jinja2 (http://jinja.pocoo.org/)

Now download webkitpony from github or install it from pypy.












