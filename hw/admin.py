from django.contrib import admin
from .models import Profile, Subject, Homework, Submission, Comment


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role')
    list_filter = ('role',)
    search_fields = ('user__username', 'user__email')


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class SubmissionInline(admin.TabularInline):
    model = Submission
    extra = 0
    readonly_fields = ('student', 'submitted_file', 'submitted_at', 'is_approved')


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0
    readonly_fields = ('user', 'text', 'created_at')


@admin.register(Homework)
class HomeworkAdmin(admin.ModelAdmin):
    list_display = ('title', 'subject', 'teacher', 'due_date', 'is_public', 'created_at')
    list_filter = ('subject', 'is_public', 'created_at')
    search_fields = ('title', 'teacher__username', 'subject__name')
    inlines = [SubmissionInline, CommentInline]
    readonly_fields = ('created_at',)


@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('homework', 'student', 'submitted_at', 'is_approved')
    list_filter = ('is_approved', 'submitted_at')
    search_fields = ('homework__title', 'student__username')
    readonly_fields = ('submitted_at',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'homework', 'created_at')
    search_fields = ('user__username', 'homework__title', 'text')
    readonly_fields = ('created_at',)
