from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import Product
from django.forms import ImageField

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Las contraseñas no coinciden.")

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data['password']
        user.set_password(password)
        
        if commit:
            user.save()
        
        return user

class SuperuserCreationForm(UserCreationForm):
    is_superuser = forms.BooleanField(label='Superusuario', required=False)

    class Meta(UserCreationForm.Meta):
        fields = ('username', 'email', 'password1', 'password2', 'is_superuser')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_staff = True  # Establecer como staff
        user.is_superuser = self.cleaned_data.get('is_superuser', False)
        
        if commit:
            user.save()
        
        return user

class UserEditForm(forms.ModelForm):
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput, required=False)
    confirm_password = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput, required=False)
    is_superuser = forms.BooleanField(label='Superusuario', required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'confirm_password', 'is_superuser')

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError('Las contraseñas no coinciden.')

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data.get('password')

        if password:
            user.set_password(password)

        user.is_staff = self.cleaned_data.get('is_superuser', False)  # Establecer como staff
        user.is_superuser = self.cleaned_data.get('is_superuser', False)

        if commit:
            if password:
                user.save()
            else:
                user.save(update_fields=['username', 'email', 'is_staff', 'is_superuser'])

        return user
    
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


        