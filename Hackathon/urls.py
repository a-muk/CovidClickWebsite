from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    path('',views.index,name='index'),
    path('index.html',views.index,name='index'),
    path('oxygen.html',views.oxygen,name='oxygen'),
    path('beds.html',views.bed,name='bed'),
    path('search',views.search,name='search'),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name= "logout"),
    path("booknow.html", views.booknow, name= 'booknow'),
    path('index',views.index,name='index'),
    
]