from django.shortcuts import render, redirect
from .models import Homework
from .forms import HomeworkForm


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
