from django.contrib import admin
from .models import Customer, Product, Order


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'address', 'reg_date')
    list_per_page = 3


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'quantity', 'date_added', 'image', 'update_date')
    list_editable = ('price', 'quantity')
    list_per_page = 3


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'total_price', 'order_date')
    list_display_links = ('id', 'customer')
    list_per_page = 3


# admin.site.register(Customer, CustomerAdmin)
# admin.site.register(Product)
# admin.site.register(Order)
