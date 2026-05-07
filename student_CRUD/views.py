from django.shortcuts import render
from .models import StudentDetail

# Create your views here.
def homepage(request):
    student_list=StudentDetail.objects.all()
    context = {
        "students": student_list
    }
    return render(request, 'homepage.html', context)
def add_student(request):
    return render(request, 'add_student.html')
