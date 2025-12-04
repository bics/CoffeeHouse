from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# class created following tutorial made by Codemy.com 
class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=50,widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'example@email.com'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
    