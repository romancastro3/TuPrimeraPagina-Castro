from django.urls import path
from django.shortcuts import redirect
from blog.views import index, registrar_usuario, login_usuario

# Redirección: si alguien entra a "/", lo mandamos al login
def home_redirect(request):
    return redirect('login_usuario')

urlpatterns = [
    path('', home_redirect, name='home_redirect'),  # Redirige la raíz al login
    path('inicio/', index, name='index'),           # El index ahora está en /inicio/
    path('registrar/', registrar_usuario, name='registrar_usuario'),
    path('login/', login_usuario, name='login_usuario'),
]
