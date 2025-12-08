from django import forms
from django.forms import ModelForm
from .models import CoffeeTable

# class created following tutorial made by Codemy.com 
class CoffeeTableForm(ModelForm):
    class Meta:
        model = CoffeeTable
        fields = ('name', 'description', 'image')

        # Code snippet generated from ChatGPT
        # This prevents Django from rendering its own <select>
        widgets = {
            "image": forms.HiddenInput(),  # or TextInput()
        }

    def __init__(self, *args, **kwargs):
        super(CoffeeTableForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['placeholder'] = 'Name your table'
        self.fields['description'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['placeholder'] = 'Describe'
