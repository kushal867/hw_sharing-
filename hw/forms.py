from django import forms
from django.contrib.auth.models import User
from .models import Homework, Submission, Comment, Profile



#   PROFILE FORM

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['role', 'bio', 'profile_image']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Write a short bio...'}),
        }



#   HOMEWORK CREATION FORM (for teachers)

class HomeworkForm(forms.ModelForm):
    class Meta:
        model = Homework
        fields = ['subject', 'title', 'chapter_name', 'instructions', 'file', 'due_date', 'is_public']
        widgets = {
            'instructions': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Write homework details...'}),
            'due_date': forms.DateInput(attrs={'type': 'date'}),
        }



# SUBMISSION FORM (for students)

class SubmissionForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ['submitted_file']
        widgets = {
            'submitted_file': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }


# COMMENT FORM

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 2, 'placeholder': 'Write your comment here...'}),
        }
