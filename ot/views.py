from django.contrib.auth.decorators import login_required  # AÑADIR ESTA LÍNEA
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.contrib.messages import get_messages

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            try:
                user = form.save()
                messages.success(request, 'Su usuario ha sido creado exitosamente.')
                return redirect('login')  # Redirige a la página de login
            except Exception as e:
                messages.error(request, f'Error al guardar el usuario: {str(e)}')
        else:
            messages.error(request, 'Datos no válidos. Por favor, corrígelos e intenta de nuevo.')
    else:
        form = CustomUserCreationForm()

    return render(request, 'register.html', {'form': form})



def login_view(request):
    # Limpiar mensajes al cargar la página
    storage = get_messages(request)
    storage.used = True

    # Si el usuario ya está autenticado, redirigir al dashboard
    if request.user.is_authenticated:
        return redirect('dashboard')

    # Manejar solicitud POST para autenticación
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Bienvenido de nuevo, {username}!')
                return redirect('dashboard')
            else:
                messages.error(request, 'Usuario o contraseña incorrectos.')
        else:
            messages.error(request, 'Datos ingresados no son válidos. Por favor verifica.')

    # Si el método es GET o hay un error, mostrar el formulario vacío o con errores
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

# Vista del dashboard (requiere autenticación)
@login_required
def dashboard(request):
    return render(request, 'dashboard.html')



@login_required
def profile(request):
    # Puedes añadir lógica para mostrar los detalles del perfil aquí
    return render(request, 'profile.html')  # Asegúrate de tener una plantilla `profile.html` creada en tu directorio de plantillas