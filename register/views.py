from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from register.form import CustomRegisterForm


def register(request):

    if request.method == 'POST':
        form = CustomRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomRegisterForm()

    return render(request, 'register/register.html', context={'form':form})

