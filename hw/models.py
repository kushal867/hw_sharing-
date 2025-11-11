from django.db import models
from django.contrib.auth.models import User



#   USER PROFILE

class Profile(models.Model):
    ROLE_CHOICES = (
        ('teacher', 'Teacher'),
        ('student', 'Student'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    bio = models.TextField(blank=True, null=True)
    profile_image = models.ImageField(upload_to='profiles/', blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} ({self.role})"



#   SUBJECT

class Subject(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name



#   HOMEWORK (assigned or shared)

class Homework(models.Model):
    teacher = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='assigned_homeworks'
    )
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    chapter_name = models.CharField(max_length=150, blank=True, null=True)
    instructions = models.TextField()
    file = models.FileField(upload_to='homeworks/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField(blank=True, null=True)
    is_public = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.subject.name} - {self.title}"

    class Meta:
        ordering = ['-created_at']



#   HOMEWORK SUBMISSIONS

class Submission(models.Model):
    homework = models.ForeignKey(
        Homework,
        on_delete=models.CASCADE,
        related_name='submissions'
    )
    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='submissions'
    )
    submitted_file = models.FileField(upload_to='submissions/')
    submitted_at = models.DateTimeField(auto_now_add=True)
    remarks = models.TextField(blank=True, null=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student.username} → {self.homework.title}"

    class Meta:
        ordering = ['-submitted_at']



#   COMMENTS / DISCUSSIONS

class Comment(models.Model):
    homework = models.ForeignKey(
        Homework,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.homework.title}"

    class Meta:
        ordering = ['-created_at']
