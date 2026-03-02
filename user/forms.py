from django import forms
from django.contrib.auth import authenticate

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            "placeholder": "Username",
            "class": "form-control"
        }),
        min_length=4,
        max_length=150,
        required=True
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "placeholder": "Password",
            "class": "form-control"
        }),
        min_length=6,
        required=True
    )

    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        self.user = None
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")

        if not username or not password:
            return cleaned_data

        self.user = authenticate(
            self.request,
            username=username,
            password=password
        )

        if self.user is None:
            raise forms.ValidationError("Invalid username or password.")

        if not self.user.is_active:
            raise forms.ValidationError("This account is inactive.")

        return cleaned_data

    def get_user(self):
        return self.user
