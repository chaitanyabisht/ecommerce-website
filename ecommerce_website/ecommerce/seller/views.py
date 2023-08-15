from django.shortcuts import render, redirect
from django.http import JsonResponse
import json
import datetime
from store.models import Order, OrderItem
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

def group_required(*group_names):
    """Requires user membership in at least one of the groups passed in."""
    def in_groups(u):
        if u.is_authenticated:
            if bool(u.groups.filter(name__in=group_names)) | u.is_superuser:
                return True
        return False

    return user_passes_test(in_groups, login_url='login_seller')



@group_required("Seller")
def orders(request):
    orders = Order.objects.all()
    context = {
        'orders':orders
    }
    return render(request, 'seller/orders.html', context)

@group_required("Seller")
def viewOrder(request, pk):
	order = Order.objects.get(transaction_id=pk)


    # Get all order items
	items = OrderItem.objects.all().filter(
		order = order
    )
    
	
	context = {'order':order, 'items':items}
    
	return render(request, 'seller/order.html', context)


class Login(auth_views.LoginView):
    template_name = 'seller/login.html'
    
    def get_success_url(self) -> str:
        return '/seller/'
      