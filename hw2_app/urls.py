from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('customer_orders/<int:customer_id>/', views.CustomerOrdersView.as_view(), name='customer_orders'),
    path('order/<int:pk>/', views.OrderView.as_view(), name='order'),
    path('customer_products/<int:customer_id>/<int:days>/', views.CustomerProductsView.as_view(), name='customer_products'),
]
