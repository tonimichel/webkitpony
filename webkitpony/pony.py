from jinja2 import Template
import webkit
import re
import gtk
import json
from inspector import Inspector


class WebkitPony(gtk.Window):
    '''Main Gui component. Creates the GTK window and loads the webgui. This
    is the main entrypoint of the gui client. Actually the real gui, where
    events and actions take place, lives in lib.view.webgui.
    '''
    
    
    def __init__(self, settings):
        '''Init a window, set size and instantiate the webgui.
        '''
        gtk.Window.__init__(self)
        
        self.webgui =  PonyWebView(settings)
        self.connect("destroy", self.destroy)
        self.add(self.webgui)
        self.show_all()
        
        if settings.DEBUG:
            webkitsettings = self.webgui.get_settings()
            webkitsettings.set_property("enable-developer-extras", True)
            inspector = Inspector(self.webgui.get_web_inspector())
        else:
            webview.props.settings.props.enable_default_context_menu = False
        
        self.set_size_request(settings.WIDTH, settings.HEIGHT)
        self.set_resizable(getattr(settings, 'RESIZABLE', False))
        self.set_title(getattr(settings, 'TITLE', 'Webkit Pony App'))
        self.show_all()
      
    def destroy(self, widget, data=None):
        gtk.main_quit()
        


class PonyWebView(webkit.WebView):
    '''
    Gui componet to embed webguis in desktop application. Listens for
    all click events and tries to map the clicked url views defined in urls.py.
    '''
    
    def __init__(self, settings):
        webkit.WebView.__init__(self)
        self.settings = settings
        self.connect('navigation-policy-decision-requested', self.on_link_clicked)
        self.connect('title-changed', self.on_title_changed)
        self.dispatch_action('', self)
        
        
            
    def on_link_clicked(self, webview, frame, req, action, policy_decision, data=None):
        ''' Eventlistener for click events
        '''
        uri = req.get_uri()
        if uri.startswith("file://"):
            return False
        elif uri.startswith("action:"):
          url = uri.split(":")[1]
          self.dispatch_action(url, webview)
          return 1
        else: 
            pass
        return False   


    def on_title_changed(self, webview, frame, data):
        try:
            data = json.loads(data)
        except ValueError:
            data = None
            
        if data and data.has_key('__url__'):
            if not data['__url__'].startswith('action:'):
                raise Exception('Your URL does not start with "action:"')
            self.dispatch_action(data['__url__'].split(":")[1], webview, data=data['__data__'])
            
    
    def dispatch_action(self, url, webview, data=None):
        ''' Dispatches the incoming url to a view in case a url-->view mapping
        was defined in urls.py. In case no mapping is found, a 404 is displayed.
        ''' 
        for mapping in self.settings.URLCONF:
            p = re.compile(mapping[0])
            
            if p.match(url) != None:
                setattr(webview, 'data', data) #@deprecated
                setattr(webview, 'DATA', data)
                args = [webview]
                m = p.search(url)
                for group in m.groups():
                    args.append(group)
                return mapping[1](*args)
        return view_404(webview)
        
      
      
    def render(self, tpl, context):
        render_webview(tpl, context, self)
    
    def json_response(self, data):
        self.execute_script("$(document).trigger('webkit_response', [%s])" % json.dumps(data))



def render_webview(tpl, kwargs, webview):
    template = webview.settings.TEMPLATE_ENV.get_template(tpl)
    kwargs.update({'STATIC_URL': webview.settings.STATIC_URL })
    html = template.render(kwargs)
    uri = 'file://'
    webview.load_string(html, "text/html", "utf-8", uri)  
   
    
def view_404(webgui):
    return render_webview('404.html', {}, webgui)
        
