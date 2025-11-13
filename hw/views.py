from django.shortcuts import render, redirect
from .models import Homework, Subject,Profile
from .forms import HomeworkForm,ProfileForm


#HOMEWORK SECTION 

# List all homework
def home(request):
    data = Homework.objects.all()
    context = {
        "form": data
    }
    return render(request, "home.html", context)


# Create new homework
def create_homework(request):
    if request.method == 'POST':
        form = HomeworkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = HomeworkForm()
    return render(request, "create_homework.html", {"form": form})


# Edit existing homework
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


# Delete homework
def hw_delete(request, id):
    homework = Homework.objects.get(id=id)
    homework.delete()
    return redirect('home')






#for the profile now 
def profile_list(request):
    profiles = Profile.objects.all()
    context = {
        "profiles": profiles
    }
    return render(request, "profile_list.html", context)

#for creating the profile
def profile_create(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProfileForm()
    return render(request, "profile_create.html", {"form": form})


#FOR editing the profile
def profile_edit(request, id):
    profile = Profile.objects.get(id=id)
    if request.method == 'POST':
        form = ProfileForm(request.POST,  instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_list')
    else:
        form = ProfileForm(instance=profile)
    return render(request, "profile_edit.html", {"form": form})


#for delete the profile
def profile_delete(request, id):
    profile = Profile.objects.get(id=id)
    profile.delete()
    return redirect('home')