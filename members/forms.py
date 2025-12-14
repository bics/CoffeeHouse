from django import forms
from allauth.account.forms import SignupForm, LoginForm

# Form generated using ChatGPT
class AllauthSignupForm(SignupForm):
    avatar = forms.ImageField(required=False)

    def save(self, request):
        user = super().save(request)
        user.avatar = self.cleaned_data.get("avatar")
        user.save()
        return user
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({ "class" : "form-control"})

class AllauthLoginForm(LoginForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["login"].widget.attrs.update({ "class": "form-control"})
        self.fields["password"].widget.attrs.update({ "class": "form-control"})