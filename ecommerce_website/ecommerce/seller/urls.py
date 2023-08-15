from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
	#Leave as empty string for base url
	path('', views.orders, name="seller-orders"),
    path('order/<pk>', views.viewOrder, name='seller-order'),
    path("login/", views.Login.as_view(), name="login_seller"),
    path("logout/", auth_views.LogoutView.as_view(template_name="seller/logout.html"), name="logout_seller"),
    
]