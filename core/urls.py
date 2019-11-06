from django.urls import path
from .import views
urlpatterns = [
    
    path('',views.home,name='home'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('secret/',views.secret_Page,name="secret"),
    path('secret2/',views.SecretPage.as_view(),name='secret2')
]
