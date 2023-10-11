from django.urls import path
from . import views

urlpatterns = [
    path('', views.ShopView.as_view(), name='shop'),
    path('customer_orders/<int:customer_id>/', views.CustomerOrdersView.as_view(), name='customer_orders'),
    path('order/<int:pk>/', views.OrderView.as_view(), name='order'),
    path('customer_products/<int:customer_id>/<int:days>/', views.CustomerProductsView.as_view(),
         name='customer_products'),
    path('product_update/<int:product_id>/', views.update_product, name='update_product'),
    path('product/<int:product_id>/', views.ProductView.as_view(), name='product'),
]
