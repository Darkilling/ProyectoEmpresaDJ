from django import forms
from django.contrib.auth.models import User

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

