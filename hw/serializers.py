from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile, Subject, Homework, Submission, Comment


# USER SERIALIZER
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


# PROFILE
class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = ['id', 'user', 'role', 'bio', 'profile_image']


# SUBJECT
class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'name', 'description']


# HOMEWORK
class HomeworkSerializer(serializers.ModelSerializer):
    teacher = UserSerializer(read_only=True)
    subject_name = serializers.CharField(source='subject.name', read_only=True)

    class Meta:
        model = Homework
        fields = [
            'id', 'teacher', 'subject', 'subject_name', 'title',
            'chapter_name', 'instructions', 'file', 'created_at',
            'due_date', 'is_public'
        ]


# SUBMISSION
class SubmissionSerializer(serializers.ModelSerializer):
    student = UserSerializer(read_only=True)
    homework_title = serializers.CharField(source='homework.title', read_only=True)

    class Meta:
        model = Submission
        fields = [
            'id', 'homework', 'homework_title', 'student',
            'submitted_file', 'submitted_at', 'remarks', 'is_approved'
        ]


# COMMENTS
class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'homework', 'user', 'text', 'created_at']
