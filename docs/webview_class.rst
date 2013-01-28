###################################
The webview object
###################################


The webview object is comparable with the request and response of a django request/response cycle and always
passed as first parameter to any view. The public interface provides the following methods and attributes:



``webview.render(template, context)``

Renders the webview.
Parameter ``template`` is a string specifying the path to your template relative to your project's template dir.
Parameter ``context`` is a dictionary applied as template context. Templates build upon jinja2.


``webview.json_response(data)``

Usefull in combination with the *client-side* ``webkitpony.send(url, data, callback)`` from ``webkitpony.js``.
Takes a single parameter ``data`` which must be a json-serializable data structure, e.g. a dict. Triggers the callback
method of the foregoing ``webkitpony.send`` passing data as *response*.



``webview.data``

Comparable with ``request.POST``. Provides the python deserialized dictionary of the foregoing ``webkitpony.send`` code.








