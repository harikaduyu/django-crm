from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from django.contrib.auth import login, logout
from .models import Product, Customer, Order
from .forms import OrderForm, RegisterForm
from .filters import OrderFilter


def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    total_customers = customers.count()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()
    context = {
        'orders': orders,
        'customers': customers,
        'total_orders': total_orders,
        'total_customers': total_customers,
        'delivered': delivered,
        'pending': pending
    }
    return render(request, 'accounts/dashboard.html', context)


def user_login(request):
    context = {}
    return render(request, 'accounts/login.html', context)


def user_register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # login(request, user)
            return redirect('login')
    else:
        form = RegisterForm()
    context = {'form': form}
    return render(request, 'accounts/register.html', context)


def product(request):
    products = Product.objects.all()
    return render(request, 'accounts/products.html', {'products': products})


def customer(request, pk):
    customer_instance = Customer.objects.get(id=pk)
    orders = customer_instance.order_set.all()
    order_count = orders.count()
    order_filter = OrderFilter(request.GET, queryset=orders)
    orders = order_filter.qs
    context = {
        'orders': orders,
        'customer': customer_instance,
        'order_count': order_count,
        'order_filter': order_filter
    }
    return render(request, 'accounts/customer.html', context)


def create_order_view(request, pk):
    order_form_set = inlineformset_factory(
        Customer, Order, fields=('product', 'status'), extra=10)
    customer_instance = Customer.objects.get(id=pk)
    formset = order_form_set(
        queryset=Order.objects.none(), instance=customer_instance)
    if request.method == 'POST':
        formset = order_form_set(request.POST, instance=customer_instance)
        if formset.is_valid():
            formset.save()
            return redirect('/')

    context = {'formset': formset}
    return render(request, 'accounts/order_form.html', context)


def update_order_view(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'accounts/order_form.html', context)


def delete_order_view(request, pk):
    order = Order.objects.get(id=pk)
    context = {'item': order}
    if request.method == 'POST':
        order.delete()
        return redirect('/')
    return render(request, 'accounts/delete.html', context)
