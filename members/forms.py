from django import forms
from allauth.account.forms import SignupForm

# Form generated using ChatGPT
class AllauthSignupForm(SignupForm):
    avatar = forms.ImageField(required=False)

    def save(self, request):
        user = super().save(request)
        user.avatar = self.cleaned_data.get("avatar")
        user.save()
        return user