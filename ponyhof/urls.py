from ponyhof import views


#   Define the mappings of urls and views here. 
urlconf = (
    ('^$', views.start),
    (r'^javascript-interaction$', views.javascript_interaction),
    (r'^handle-form$', views.handle_form),
  
)
