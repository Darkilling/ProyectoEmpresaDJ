from django import forms
from django.contrib.auth.models import User
from .models import Area, TipoParadero, Tarea, Material

class CustomUserCreationForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']

    # Validar que el email sea único
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este correo ya está en uso.")
        return email

    # Guardar el usuario en la base de datos
    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.username = self.cleaned_data['email']  # Usamos el correo electrónico como nombre de usuario
        user.set_password(self.cleaned_data['password'])  # Guardar la contraseña cifrada
        if commit:
            user.save()
        return user


class AreaForm(forms.Form):
    area = forms.ModelChoiceField(queryset=Area.objects.all(), label="Área de trabajo")

class TipoParaderoForm(forms.Form):
    tipo_paradero = forms.ModelChoiceField(queryset=TipoParadero.objects.none(), label="Tipo de paradero")

    def __init__(self, area_id, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tipo_paradero'].queryset = TipoParadero.objects.filter(area_id=area_id)

class TareaForm(forms.Form):
    tareas = forms.ModelMultipleChoiceField(queryset=Tarea.objects.all(), widget=forms.CheckboxSelectMultiple, label="Tareas")

class MaterialForm(forms.Form):
    materiales = forms.ModelMultipleChoiceField(queryset=Material.objects.all(), widget=forms.CheckboxSelectMultiple, label="Materiales")
    otros = forms.CharField(max_length=255, required=False, label="Otros")
    observacion = forms.CharField(widget=forms.Textarea, required=False, label="Observación")


class DatosGeneralesForm(forms.Form):
    direccion = forms.CharField(max_length=255, label="Dirección")
    comuna = forms.CharField(max_length=100, label="Comuna")
    tiempo_estimado = forms.CharField(max_length=50, label="Tiempo Estimado")
    ceco = forms.CharField(max_length=100, label="CeCo")
    jefe_proyecto = forms.CharField(max_length=100, label="Jefe de Proyecto")
    supervisor = forms.CharField(max_length=100, label="Supervisor")
    cliente = forms.CharField(max_length=100, label="Cliente")
    otros = forms.CharField(max_length=255, required=False, label="Otros")
    observacion = forms.CharField(widget=forms.Textarea, required=False, label="Observación")

