from django.conf.urls import url
from django.contrib.auth import views as auth_views #django login and logout views
from . import views

app_name = 'accounts' #needed for url templates

urlpatterns = [
    url(r'login/$', auth_views.LoginView.as_view(template_name='accounts/login.html'),name='login'),
    url(r'logout/$', auth_views.LogoutView.as_view(), name='logout'), #uses django view so no need to assign template_name
    url(r'signup/$', views.SignUp.as_view(), name='signup'),
]
