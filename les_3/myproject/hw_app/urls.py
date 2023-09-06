from django.urls import path
from . import views

urlpatterns = [
    path('client/<int:client_id>/', views.client_orders, name='client_orders'),
    path('client/<int:client_id>/<int:term>', views.orders_term, name='orders_term'),
    path('goods/<int:goods_id>/', views.goods_description, name='goods_description'),
]