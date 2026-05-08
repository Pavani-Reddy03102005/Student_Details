from django.shortcuts import render, redirect, get_object_or_404
from .models import StudentDetail
from .forms import StudentForm

def homepage(request):
    students_list = StudentDetail.objects.all()
    context = {
        "students": students_list
    }
    return render(request, "homepage.html", context)

def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("homepage")
    else:
        form = StudentForm()

    return render(request, "add_student.html", {"form": form})
def details(request, id):
    student = get_object_or_404(StudentDetail, pk=id)
    form = StudentForm(instance=student)

    return render(request, "view_details.html", {"form": form})

def update_student(request, id):
    student = StudentDetail.objects.get(id=id)

    if request.method == "POST":
        student.student_name = request.POST.get("student_name")
        student.email = request.POST.get("email")
        student.course = request.POST.get("course")
        student.enrollment_date = request.POST.get("enrollment_date")
        student.save()
        return redirect("homepage")

    context = {
        "student": student
    }

    return render(request, "update.html", context)   # ✅ FIXED
def delete_student(request, id):
    student = get_object_or_404(StudentDetail, id=id)
    student.delete()
    return redirect("homepage")