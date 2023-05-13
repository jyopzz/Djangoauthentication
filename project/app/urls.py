from django.urls import path,include
from .views import loginn
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
urlpatterns = [
    #path('', loginn),
    path ('accounts/',include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'),name='home')
]