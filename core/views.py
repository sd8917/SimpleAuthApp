from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def home(request):
    count = User.objects.count()
    return render(request,'home.html',{'count':count})

def signup(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST) # This is used to create a user 
        if form.is_valid:
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request,'registration/signup.html',{'form': form})

def login(request):
    return render(request, 'registration/login.html')


@login_required
def secret_Page(request):
    return render(request,'secret_page.html')

class SecretPage(LoginRequired,MixinTemplateView):
    template_name = 'secret_page.html'
