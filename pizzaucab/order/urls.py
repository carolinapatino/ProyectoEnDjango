from django.urls import path
from django.conf.urls import include, url
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    url(r'^$', views.index, name='index'),
    url(r'details', views.orderDetail, name='orderDetail'),
    # path('<int:order_id>/', views.detail, name='detail'),
    # path('nuevo', views.addPizza, name='addPizza'),
    url(r'addPizza', views.addPizza, name='addPizza'),
    # path('addPizza/<int:order_id>', views.addPizza, name='addPizza'),
    path('deletePizza/<int:id>', views.deletePizza, name='deletePizza'),
    url(r'Reports', views.Reports, name='reports'),
    url(r'OrdersReport', views.orders, name='orders'),
    path('OrdersBySize/<size>', views.ordersBySize, name='ordersBySize'),
    path('OrdersByIngredient/<ingredient>', views.ordersByIngredient, name='ordersByIngredient'),
    path('OrdersByClient/<client>', views.ordersByClient, name='ordersByClient'),
]