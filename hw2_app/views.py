from django.utils import timezone
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404
from .models import Customer, Order


class HomeView(TemplateView):
    template_name = 'hw2_app/home.html'

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
        products = [product for order in orders for product in order.products.all()]
        context['products'] = set(products)
        return context
