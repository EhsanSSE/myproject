from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class MyAuthenticationForm(AuthenticationForm):
    def clean(self):
        username_or_email = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if username_or_email and password:
            user = None

            if "@" in username_or_email:
                try:
                    user = User.objects.get(email=username_or_email)
                    username_or_email = user.username
                except User.DoesNotExist:
                    raise forms.ValidationError("⚠ No account found with this email.")

            self.user_cache = authenticate(username=username_or_email, password=password)
            if self.user_cache is None:
                raise forms.ValidationError("⚠ Invalid username/email or password.")

        return self.cleaned_data