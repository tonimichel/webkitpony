###################################
The webkitpony.js
###################################

The ``webkitpony.js`` contains Javascript utils to enable the communication between the UI and the python-side 
of your application. At the moment webkitpony.js requires jQuery, which is inlcuded in the download package.

For now ``webkitpony.js`` provides a single method:

``webkitpony.send(url, data, callback)``

Parameter ``url`` is the url being processed by the pony's url dispatcher. ``data`` is a json-serializable object
which is sent to the application being available in our views via ``webview.DATA``. ``callback`` is a simple function
taking a single parameter ``response``. ``response`` contains the data sent back by the application.


