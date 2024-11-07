from django import forms
from django.contrib.auth.models import User
from .models import OTFormulario

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

class OTFormularioForm(forms.ModelForm):
    class Meta:
        model = OTFormulario
        fields = [
            'cliente',
            'direccion',
            'comuna',
            'tiempo_estimado',
            'CECO',
            'jefe_proyecto',
            'supervisor',
            'planificacion_material',
            'observacion'
        ]
        widgets = {
            'observacion': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }