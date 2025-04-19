from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.urls import reverse


def login_view(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('shopapp:index'))
        return render(request, 'myauth/login.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect('shopapp:products_list')
        return render(request, 'myauth/login.html', {'error': 'Invalid login credentials'})