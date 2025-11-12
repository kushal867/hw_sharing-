from django import forms
from django.contrib.auth.models import User
from .models import Homework, Submission, Comment, Profile


class HomeworkForm(forms.ModelForm):
    class Meta:
        model = Homework
        fields = "__all__"

class SubmissionForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = "__all__"



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = "__all__"



class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"