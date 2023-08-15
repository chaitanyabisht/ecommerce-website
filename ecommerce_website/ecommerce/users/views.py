from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CustomerRegisterForm, CustomerUpdateForm, UserUpdateForm

def register(request):

    if request.method == "POST":
        u_form = UserCreationForm(request.POST)
        c_form = CustomerRegisterForm(request.POST)
        # add user to c_form
        c_form.instance.user = u_form.instance
        if (u_form.is_valid() and c_form.is_valid()):
            u_form.save()
            c_form.save()
            return redirect('login')

    else:
        u_form = UserCreationForm()
        c_form = CustomerRegisterForm()
        return render(request, 'users/register.html', {'u_form':u_form, 'c_form':c_form})
    

def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        c_form = CustomerUpdateForm(request.POST, instance=request.user.customer)
        # add user to c_form
        # c_form.instance.user = u_form.instance
        if (u_form.is_valid() and c_form.is_valid()):
            u_form.save()
            c_form.save()
            return redirect('profile')
        else:
            messages.warning(request, 'Please correct the error below.')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        c_form = CustomerUpdateForm(instance=request.user.customer)
        return render(request, 'users/profile.html', {'u_form':u_form, 'c_form':c_form})