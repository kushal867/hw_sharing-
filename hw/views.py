from django.shortcuts import render, redirect
from .models import Homework, Submission, Comment, Profile
from .forms import  HomeworkForm, SubmissionForm, CommentForm, ProfileForm
# Create your views here.

def home(request):
    data = Homework.objects.all()
    context = {
        "form":data
    }
    return render(request, "home.html", context)

#for homework

def create_homework(request):
    if request.method == 'POST':
        form = HomeworkForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            form =  HomeworkForm()
            return render(request, "create_homework.html", {"form":form})
        
#edit for homework

def edit_homework(request, id):
    homeworks= Homework.objects.get(id=id)
    form = HomeworkForm(request.POST,instance=id)
    if request.method == 'POST':
        form = HomeworkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            form = HomeworkForm()
            return render(request, "edit_homework.html", {"form":form})


#homework delete
def hw_delete(request, id):
    homeworks = Homework.objects.get(id=id)
    homeworks.delete(request.POST)
    return redirect(home)


