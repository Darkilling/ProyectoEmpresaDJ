from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.login_view, name='home'),  # Página principal, es el login
    path('login/', views.login_view, name='login'),  # Alias para la vista de login
    path('register/', views.register, name='register'),  # Registro de usuario
    path('dashboard/', views.dashboard, name='dashboard'),  # Dashboard que requiere autenticación
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),  # Cerrar sesión
    path('profile/', views.profile, name='profile'),  # Nueva ruta para revisar el perfil

    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='password_change.html'), name='password_change'),
    path('password_change_done/', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'), name='password_change_done'),
]
