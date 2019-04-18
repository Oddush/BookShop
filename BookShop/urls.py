from django.conf.urls import url
from django.views.generic import TemplateView
from BookShop import views

app_name = 'BookShop'
urlpatterns = [

    ##Requests

    ## Registration
    # Parameters: name, email, password
    # Method: POST
    url(r'^register/$', views.RegisterFormView.as_view()),
    ## Authentication
    # Parameters: name/email, password
    # Method: POST
    url(r'^login/$', views.LoginFormView.as_view()),
    url(r'^logout/$', views.LogoutView.as_view()),
    url(r'^$', TemplateView.as_view(template_name='home.html')),
    ## Products
    # Parameters: ID, price, name
    # Method: GET
    url(r'^product/$', views.product, name='product'),
    ## Sort of Products by max
    # Parameters: max
    # Method: POST
    url(r'^product/?select=max', views.product, name='product'),
    ## Sort of Products by min
    # Parameters: min
    # Method: POST
    url(r'^product/?select=min', views.product, name='product'),
    ## Users
    # Parameters: name, email
    # Method: GET
    url(r'^contact/$', views.contact, name='contact'),
]
