from django.urls import path
from django.conf.urls import include, url
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    url(r'^$', views.index, name='index'),
    path('<int:order_id>/', views.detail, name='detail'),
    # path('nuevo', views.addPizza, name='addPizza'),
    url(r'nuevo', views.addPizza, name='addPizza'),
]