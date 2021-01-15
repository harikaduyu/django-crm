from django.shortcuts import render, redirect

from .models import Product, Customer, Order
from .forms import OrderForm


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


def product(request):
    products = Product.objects.all()
    return render(request, 'accounts/products.html', {'products': products})


def customer(request, pk):
    customer_instance = Customer.objects.get(id=pk)
    orders = customer_instance.order_set.all()
    order_count = orders.count()
    context = {
        'orders': orders,
        'customer': customer_instance,
        'order_count': order_count
    }
    return render(request, 'accounts/customer.html', context)


def create_order(request):
    form = OrderForm()
    if request.method == 'POST':
        # print('Printing Post', request.POST)
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'accounts/order_form.html', context)
