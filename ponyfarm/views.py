# -*- coding: utf-8 -*-
from webkitpony.pony import render_webview
import datetime



def start(webview):
    webview.render('start.html', {})
    
def examples(webview):
    webview.render('examples.html', {'about': True,})
    
def full_reload(webview):
    webview.render('examples.html', {'full_reload': True})
    
def pseudo_ajax(webview):
    webview.render('examples.html', {'pseudo_ajax': True,})
    
def tipps(webview):
    webview.render('examples.html', {'tipps': True,})

def send_message(webview):
    return webview.json_response({
        'timestamp': str(datetime.datetime.now()),
        'original_data': webview.DATA
    })
    
    
    
    
    
    
    
