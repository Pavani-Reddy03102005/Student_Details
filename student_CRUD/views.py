from urllib import request

from django.shortcuts import redirect, render
from .models import StudentDetail
from .forms import StudentForm

# Create your views here.
def homepage(request):
    student_list=StudentDetail.objects.all()
    context = {
        "students": student_list
    }
    return render(request, 'homepage.html', context)
def add_student(request):
    if request.method=="POST":
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage') 
    else:
        form=StudentForm()
    context={
        "form": form
    }
    return render(request, 'add_student.html', context)