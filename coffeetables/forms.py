from django import forms
from django.forms import ModelForm
from .models import CoffeeTable, Reply

# class created following tutorial made by Codemy.com 
class CoffeeTableForm(ModelForm):
    class Meta:
        model = CoffeeTable
        fields = ('name', 'description', 'image')

        # Code snippet generated from ChatGPT
        # This prevents Django from rendering its own <select>
        widgets = {
            "name": forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Name your table'}),
            "description": forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Describe'}),
            "image": forms.HiddenInput(),  # or TextInput()
        }

class ReplyForm(ModelForm):
    class Meta:
        model = Reply
        fields = ('message',)

        widgets = {
            "message": forms.Textarea(attrs={'class':'form-control'})
        }

class UpdateReplyForm(ModelForm):
    class Meta:
        model = Reply
        fields = ('message',)

        widgets = {
            "message": forms.Textarea(attrs={'class':'form-control'})
        }