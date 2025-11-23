from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile, Subject, Homework, Submission, Comment

# ------------------------
# USER SERIALIZER
# ------------------------
class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'full_name']

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}" if obj.first_name or obj.last_name else obj.username


# ------------------------
# PROFILE SERIALIZER
# ------------------------
class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = ['id', 'user', 'role', 'bio', 'profile_image']


# ------------------------
# SUBJECT SERIALIZER
# ------------------------
class SubjectSerializer(serializers.ModelSerializer):
    teacher_count = serializers.SerializerMethodField()

    class Meta:
        model = Subject
        fields = ['id', 'name', 'description', 'teacher_count']

    def get_teacher_count(self, obj):
        # Assuming you have a related name in Homework model like `subject.homework_set`
        return obj.homework_set.values('teacher').distinct().count()


# ------------------------
# HOMEWORK SERIALIZER
# ------------------------
class HomeworkSerializer(serializers.ModelSerializer):
    teacher = UserSerializer(read_only=True)
    subject_name = serializers.CharField(source='subject.name', read_only=True)
    submissions_count = serializers.SerializerMethodField()

    class Meta:
        model = Homework
        fields = [
            'id', 'teacher', 'subject', 'subject_name', 'title',
            'chapter_name', 'instructions', 'file', 'created_at',
            'due_date', 'is_public', 'submissions_count'
        ]

    def get_submissions_count(self, obj):
        return obj.submission_set.count()


# ------------------------
# SUBMISSION SERIALIZER
# ------------------------
class SubmissionSerializer(serializers.ModelSerializer):
    student = UserSerializer(read_only=True)
    homework_title = serializers.CharField(source='homework.title', read_only=True)
    remarks_preview = serializers.SerializerMethodField()

    class Meta:
        model = Submission
        fields = [
            'id', 'homework', 'homework_title', 'student',
            'submitted_file', 'submitted_at', 'remarks', 'remarks_preview',
            'is_approved'
        ]

    def get_remarks_preview(self, obj):
        return obj.remarks[:50] + '...' if obj.remarks and len(obj.remarks) > 50 else obj.remarks


# ------------------------
# COMMENT SERIALIZER
# ------------------------
class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_name = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'homework', 'user', 'user_name', 'text', 'created_at']
