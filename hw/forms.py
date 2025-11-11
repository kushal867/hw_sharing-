from django import forms
from django.contrib.auth.models import User
from .models import Homework, Submission, Comment, Profile


class HomeworkForm(forms.ModelForm):
    class Meta:
        model = Homework
        fields = "__all__"