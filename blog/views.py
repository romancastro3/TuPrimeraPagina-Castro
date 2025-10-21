from django.shortcuts import render, redirect
from django.contrib import messages
from blog.forms import UsuarioForm, LoginForm
from blog.models import Usuario, Post

def index(request):
    consulta = request.GET.get('consulta', '')
    if consulta:
        posts = Post.objects.filter(titulo__icontains=consulta) | Post.objects.filter(categoria__nombre__icontains=consulta)
    else:
        posts = Post.objects.all().order_by('-fecha_creacion')
    return render(request, 'blog/index.html', {'posts': posts, 'consulta': consulta})


def registrar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']

            if Usuario.objects.filter(email=email).exists():
                messages.error(request, 'El correo ya está registrado. Intenta iniciar sesión.')
            else:
                form.save()
                messages.success(request, 'Registro exitoso. Ahora puedes iniciar sesión.')
                return redirect('login_usuario')
    else:
        form = UsuarioForm()
    
    return render(request, 'blog/registrar_usuario.html', {'form': form})




def login_usuario(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            contraseña = form.cleaned_data['contraseña']

            try:
                usuario = Usuario.objects.get(email=email, contraseña=contraseña)
                request.session['usuario_id'] = usuario.id
                request.session['usuario_nombre'] = usuario.nombre
                messages.success(request, f'¡Bienvenido {usuario.nombre}!')
                return redirect('index')
            except Usuario.DoesNotExist:
                messages.error(request, 'Correo o contraseña incorrectos.')
    else:
        form = LoginForm()

    return render(request, 'blog/login.html', {'form': form})




