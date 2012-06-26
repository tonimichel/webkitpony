from jinja2 import Template
import webkit
import re
import gtk



class WebkitPony(gtk.Window):
    '''Main Gui component. Creates the GTK window and loads the webgui. This
    is the main entrypoint of the gui client. Actually the real gui, where
    events and actions take place, lives in lib.view.webgui.
    '''
    
    
    def __init__(self, settings):
        '''Init a window, set size and instantiate the webgui.
        '''
        gtk.Window.__init__(self)
        self.webgui =  WebGui(settings)
        self.set_default_size(settings.WIDTH, settings.HEIGHT)
        self.connect("destroy", self.destroy)
        self.add(self.webgui)
        self.show_all()
      
    def destroy(self, widget, data=None):
        gtk.main_quit()
        


class WebGui(webkit.WebView):
    '''
    Gui componet to embed webguis in desktop application. Listens for
    all click events and tries to map the clicked url views defined in urls.py.
    '''
    
    def __init__(self, settings):
        webkit.WebView.__init__(self)
        self.settings = settings
        self.connect('navigation-policy-decision-requested', self.on_link_clicked)
        self.dispatch_action('', self)
        
    def on_link_clicked(self, webgui, frame, req, action, policy_decision, data=None):
        ''' Eventlistener for click events
        '''
        uri = req.get_uri()
        if uri.startswith("file://"):
            return False
        elif uri.startswith("action:"):
          url = uri.split(":")[1]
          self.dispatch_action(url, webgui)
        else: 
            pass
        return False   
    
    
    def dispatch_action(self, url, webgui):
        ''' Dispatches the incoming url to a view in case a url-->view mapping
        was defined in urls.py. In case no mapping is found, a 404 is displayed.
        ''' 
        
        for mapping in self.settings.URLCONF:
            p = re.compile(mapping[0])
            
            if p.match(url) != None:
                args = [webgui]
                m = p.search(url)
                for group in m.groups():
                    args.append(group)
                       
                return mapping[1](*args)
                                  

        return view_404(webgui)
        




def render_webview(tpl, kwargs, webgui):
    template = webgui.settings.TEMPLATE_ENV.get_template(tpl)
    kwargs.update({'STATIC_URL': webgui.settings.STATIC_URL })
    html = template.render(kwargs)
    uri = 'file://'
    webgui.load_string(html, "text/html", "utf-8", uri)  
   
    
def view_404(webgui):
    return render_webview('404.html', {}, webgui)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    
