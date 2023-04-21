from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail


# Create your views here.

def send_email(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        destination = request.POST.get("email")
        sender = 'okoloebelechukwu93@gmail.com'
        message = request.POST.get("message")
        send_mail(title, message, sender, [destination], fail_silently=False)
        return HttpResponse('sent')

    return HttpResponse('send mail')
