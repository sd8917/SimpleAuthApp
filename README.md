# SimpleAuthApp
* An app auth in django

### Templates structure
>Since the default template directory is inside the app so config your setting

#### settings.py

```
Inside the templates
'DIRS': [ os.path.join(BASE_DIR, 'mysite/templates')

LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

```
>main_project/templates/base.html

>main_project/templates/home.html

>main_project/templates/secret_page.html

>main_project/templates/registration/signup.html

>further as follow:-
```
accounts/login/ [name='login']
accounts/logout/ [name='logout']
accounts/password_change/ [name='password_change']
accounts/password_change/done/ [name='password_change_done']
accounts/password_reset/ [name='password_reset']
accounts/password_reset/done/ [name='password_reset_done']
accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
accounts/reset/done/ [name='password_reset_complete']

```
[Django Auth](https://docs.djangoproject.com/en/2.2/topics/auth/default/)


### urls.py of main project
```
  path('',include('core.urls')), #For register
  path('accounts/', include('django.contrib.auth.urls')),
  
```

### urls.py of app
```
    path('',views.home,name='home'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('secret/',views.secret_Page,name="secret"),
    path('secret2/',views.SecretPage.as_view(),name='secret2')
```

#### signup view

```
def signup(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST) # This is used to create a user 
        if form.is_valid:
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request,'registration/signup.html',{'form': form})
    
```

#### login view

``` 
#Everything will be handled by django.contrib.auth
def login(request):
    return render(request, 'registration/login.html')
    
```

### FOR DECORATOR OF LOGIN 

```
# FUNCTION BASED VIEW
@login_required
def secret_Page(request):
    return render(request,'secret_page.html')

# CLASS BASED VIEW
class SecretPage(LoginRequiredMixin,TemplateView):
    template_name = 'secret_page.html'

```
### Note:- we have to import these

```
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

```

## base.html
```
{% if user.is_authenticated %}
#do something
{% else %}
#do other thing
{% endif %}
```

### signup.html

```
# This will create the user form is the user imported UserCreationForm in views.py
{{ form.as_p}}

```

* For further Qwery go through the doc and youtube video
[Youtube auth](https://www.youtube.com/watch?v=Sy8dVjJqLHI&list=PLLxk3TkuAYnryu1lEcFaBr358IynT7l7H&index=8)

[Django official doc for Auth](https://docs.djangoproject.com/en/2.2/topics/auth/default/)
