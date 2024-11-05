from django.contrib.auth.decorators import login_required  # AÑADIR ESTA LÍNEA
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.contrib.messages import get_messages
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from .forms import AreaForm, TipoParaderoForm, TareaForm, MaterialForm, DatosGeneralesForm
from .models import Area, TipoParadero, Tarea, Material, Seleccion
from .forms import SeleccionForm



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


@login_required
def guardar_seleccion(request):
    if request.method == 'POST':
        form = DatosGeneralesForm(request.POST)
        if form.is_valid():
            seleccion = Seleccion.objects.create(
                area_id=request.session.get('area_id'),
                tipo_paradero_id=request.session.get('tipo_paradero_id'),
                direccion=form.cleaned_data['direccion'],
                comuna=form.cleaned_data['comuna'],
                tiempo_estimado=form.cleaned_data['tiempo_estimado'],
                ceco=form.cleaned_data['ceco'],
                jefe_proyecto=form.cleaned_data['jefe_proyecto'],
                supervisor=form.cleaned_data['supervisor'],
                cliente=form.cleaned_data['cliente'],
                otros=form.cleaned_data['otros'],
                observacion=form.cleaned_data['observacion'],
            )
            seleccion.tareas.set(request.session.get('tareas'))
            seleccion.materiales.set(request.session.get('materiales'))
            return redirect('vista_guia')
    else:
        form = DatosGeneralesForm()
    return render(request, 'guardar_seleccion.html', {'form': form})

@login_required
def vista_guia(request, seleccion_id):
    seleccion = Seleccion.objects.get(id=seleccion_id)
    return render(request, 'vista_guia.html', {'seleccion': seleccion})


@login_required
def seleccionar_area(request):
    if request.method == 'POST':
        form = AreaForm(request.POST)
        if form.is_valid():
            request.session['area_id'] = form.cleaned_data['area'].id
            return redirect('seleccionar_tipo_paradero')
    else:
        form = AreaForm()
    return render(request, 'seleccionar_area.html', {'form': form})

@login_required
def seleccionar_tipo_paradero(request):
    area_id = request.session.get('area_id')
    if not area_id:
        return redirect('seleccionar_area')
    if request.method == 'POST':
        form = TipoParaderoForm(area_id, request.POST)
        if form.is_valid():
            request.session['tipo_paradero_id'] = form.cleaned_data['tipo_paradero'].id
            return redirect('seleccionar_tareas')
    else:
        form = TipoParaderoForm(area_id)
    return render(request, 'seleccionar_tipo_paradero.html', {'form': form})

@login_required
def seleccionar_tareas(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            request.session['tareas'] = [t.id for t in form.cleaned_data['tareas']]
            return redirect('seleccionar_materiales')
    else:
        form = TareaForm()
    return render(request, 'seleccionar_tareas.html', {'form': form})

@login_required
def seleccionar_materiales(request):
    if request.method == 'POST':
        form = MaterialForm(request.POST)
        if form.is_valid():
            seleccion = Seleccion.objects.create(
                area_id=request.session.get('area_id'),
                tipo_paradero_id=request.session.get('tipo_paradero_id'),
                otros=form.cleaned_data['otros'],
                observacion=form.cleaned_data['observacion'],
            )
            seleccion.tareas.set(request.session.get('tareas'))
            seleccion.materiales.set(form.cleaned_data['materiales'])
            return redirect('resultado')
    else:
        form = MaterialForm()
    return render(request, 'seleccionar_materiales.html', {'form': form})

@login_required
def lista_OT(request):
    seleccion = Seleccion.objects.all()
    return render(request, 'lista_OT.html', {'seleccion': seleccion})

@login_required
def crear_seleccion(request):
    if request.method == 'POST':
        form = SeleccionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Redirige a la página que desees después de guardar
    else:
        form = SeleccionForm()
    return render(request, 'crear_seleccion.html', {'form': form})