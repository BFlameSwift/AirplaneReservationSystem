"""AirplaneReservationSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic.base import TemplateView

import kernel.views
from login import views
from background.views import entry_flight
from background.views import delete_flight,setting_new_flight
from kernel.views import *
from django.urls import include

from login.views import *
urlpatterns = [
    path('',TemplateView.as_view(template_name="index.html")),

    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('api/login/', views.login),
    path('api/register/', views.register),
    path('api/logout/', views.logout),
    # path('captcha/',include('captcha.urls')),
    path('confirm/', views.user_confirm),
    path('api/background/entry_flight/',entry_flight),
    path('api/background/delete_flight/',delete_flight),
    path('api/background/produce_flight/',setting_new_flight),

    path('api/query_flight/',query_flight),

    path('api/book_ticket/',kernel.views.book_ticket),
    path('api/cancel_ticket/',kernel.views.cancel_ticket),

    path('api/pay/', kernel.views.paysView, name='pays'),
    # TODO 支付后返回的url

    path('test_ajax/',include('test_ajax.urls'))

]
