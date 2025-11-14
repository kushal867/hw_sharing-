from django.shortcuts import render, redirect
from .models import Homework, Profile, Comment
from .forms import HomeworkForm, ProfileForm, CommentForm


# HOMEWORK SECTION

def home(request):
    data = Homework.objects.all()
    context = {
        "form": data
    }
    return render(request, "home.html", context)


def create_homework(request):
    if request.method == 'POST':
        form = HomeworkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = HomeworkForm()
    return render(request, "create_homework.html", {"form": form})


def edit_homework(request, id):
    homework = Homework.objects.get(id=id)

    if request.method == 'POST':
        form = HomeworkForm(request.POST, instance=homework)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = HomeworkForm(instance=homework)

    return render(request, "edit_homework.html", {"form": form})


def hw_delete(request, id):
    homework = Homework.objects.get(id=id)
    homework.delete()
    return redirect('home')



# PROFILE SECTION

def profile_list(request):
    profiles = Profile.objects.all()
    context = {
        "profiles": profiles
    }
    return render(request, "profile_list.html", context)


def profile_create(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProfileForm()

    return render(request, "profile_create.html", {"form": form})


def profile_edit(request, id):
    profile = Profile.objects.get(id=id)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_list')
    else:
        form = ProfileForm(instance=profile)

    return render(request, "profile_edit.html", {"form": form})


def profile_delete(request, id):
    profile = Profile.objects.get(id=id)
    profile.delete()
    return redirect('home')



# COMMENT SECTION

def comment_list(request):
    comments = Comment.objects.all()
    context = {
        "comment": comments
    }
    return render(request, "comment_list.html", context)


def create_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CommentForm()

    return render(request, "create_comment.html", {"form": form})


def edit_comment(request, id):
    comment = Comment.objects.get(id=id)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CommentForm(instance=comment)

    return render(request, "edit_comment.html", {"form": form})


def comment_delete(request, id):
    comment = Comment.objects.get(id=id)
    comment.delete()
    return redirect('home')
