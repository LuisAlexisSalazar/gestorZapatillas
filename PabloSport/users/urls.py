from django.urls import path
from users import views

# Nos ayuda a deslogearse -> logout

from django.contrib.auth.views import LoginView,LogoutView


# Django nos proporciona herramientas para validar la autentificacion del usuario para permitir accede la ruta
from django.contrib.auth.decorators import login_required

urlpatterns = [
    
    # path('home',views.home,name="Home"),

    # Llamdo a la funcion nos indica que es necesario aver iniciado sesion con un usuario
    path('home',login_required(views.home),name="Home"),
    
    path('',LoginView.as_view(template_name = 'users/login.html'),name='Login'),

    path('logout',LogoutView.as_view(),name='Logout'),
]

