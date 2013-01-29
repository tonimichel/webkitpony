from ponyfarm import views


#   Define the mappings of urls and views here. 
urlconf = (
    ('^$', views.start),
    ('^start/$', views.start),
    (r'^examples/$', views.examples),
    (r'^full_reload/$', views.full_reload),
    (r'^pseudo_ajax/$', views.pseudo_ajax),
    (r'^tipps/$', views.tipps),
    
    (r'^send_message/$', views.send_message),
  
)
