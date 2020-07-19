from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):

    return render(request, 'index.html')

@login_required(login_url='/accounts/login/')
def send_email(request):
    current_user = request.user
    email = current_user.email
    name = current_user.username
    send_welcome_email(name, email)
    return redirect(new_profile)