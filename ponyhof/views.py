# -*- coding: utf-8 -*-
from webkitpony.pony import render_webview
import json


def start(webview):

    webview.render('start.html', {
        'start': True, 
    })
    
def javascript_interaction(webview):

    webview.render('interaction.html', {
        'about': True, 
    })

  


def handle_form(webview):
        
    return webview.json_response({'message': 'This is the server generated response', 'original_data': webview.data})
    
    
    
    
    
    
    
