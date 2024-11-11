from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, HttpResponseBadRequest
from django.views import View
from django.urls import reverse

#model
from userlogin.models import Master_User as m_user

#declaration function check email
from support.support_function import check_is_email

#method login logout auth request
from django.contrib.auth import login, authenticate, logout

#login required methon decorator
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

import re

@method_decorator(login_required(), name='dispatch')
class IndexViews(View):
    def get(self, request):
        data = {
            'page_title': 'Dashboard',
        }

        return render(request, 'index.html', data)

class LoginViews(View):
    def get(self, request):
        data = {
            'page_title': 'Dashboard',
        }

        return render(request, 'login.html', data)

    def post(self, request):
        email=request.POST.get('staticEmail')
        password=request.POST.get('inputPassword')

        #check is email or username
        is_email = check_is_email(email)

        if is_email:
            try:
                user = m_user.objects.get(email=email, password=password)
                # user = authenticate(request, email=email, password=password)
                login(request, user)
            except Exception as e:
                return redirect('userlogin:login')
        else:
            try:
                user = m_user.objects.get(username=email, password=password)
                login(request, user)
            except Exception as e:
                return redirect('userlogin:login')

        data = {
            'page_title': 'Dashboard',
        }
        # return render(request, 'index.html', data)
        return redirect('userlogin:index')

class LogoutViews(View):
    def get(self, request):
        logout_message = request.GET.get('logout_message', None)
        if logout_message is not None:
            messages.info(request, logout_message)
        
        logout(request)
        return redirect(request.META['HTTP_REFERER'])