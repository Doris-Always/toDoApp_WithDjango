from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('sendemail/',csrf_exempt(views.send_email))
]
