from django.urls import path, include, re_path
from django.conf.urls import url, handler403
from .views import akun

app_name = 'userlogin'

urlpatterns = [
   path('', akun.IndexViews.as_view(), name = 'index'),
   path('login/', akun.LoginViews.as_view(), name = 'login'),
   path('logout/', akun.LogoutViews.as_view(), name = 'logout'),
]
