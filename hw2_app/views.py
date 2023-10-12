from django.utils import timezone
from django.urls import reverse
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404, redirect, render
from .models import Customer, Order, Product
from .forms import ProductForm


class ShopView(TemplateView):
    template_name = 'hw2_app/shop.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная'
        return context


class CustomerOrdersView(TemplateView):
    template_name = 'hw2_app/customer_orders.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        customer_id = self.kwargs.get('customer_id')
        context['title'] = 'Заказы клиента'
        customer = get_object_or_404(Customer, pk=customer_id)
        context['customer'] = customer
        orders = Order.objects.filter(customer=self.kwargs.get('customer_id')).all()
        context['orders'] = orders
        return context


class OrderView(TemplateView):
    template_name = 'hw2_app/order.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'О заказе'
        order = Order.objects.get(pk=self.kwargs['pk'])
        context['order'] = order
        products = order.products.all()
        context['products'] = products
        return context


class CustomerProductsView(TemplateView):
    template_name = 'hw2_app/customer_products.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Товары клиента'
        customer = get_object_or_404(Customer, pk=self.kwargs['customer_id'])
        context['customer'] = customer
        days = self.kwargs['days']
        context['days'] = days
        orders = Order.objects.filter(customer=customer,
                                      order_date__gte=(timezone.now() - timezone.timedelta(days=days))).all()
        products = [product for order in orders.prefetch_related('products') for product in order.products.all()]
        context['products'] = set(products)
        return context


def update_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        product = ProductForm(request.POST, request.FILES, instance=product)
        if product.is_valid():
            product.save()
            return redirect(reverse('product', kwargs={'product_id': product_id}))
    else:
        form = ProductForm(instance=product)
        return render(request, 'hw2_app/update_product.html', {'form': form, 'title': 'Редактирование товара'})


class ProductView(TemplateView):
    template_name = 'hw2_app/product.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = get_object_or_404(Product, pk=self.kwargs['product_id'])
        context['product'] = product
        context['title'] = 'Информация о товаре'
        return context
