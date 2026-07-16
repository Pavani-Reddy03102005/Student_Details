from django.shortcuts import render, redirect, get_object_or_404
from .models import StudentDetail
from .forms import StudentForm

from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import StudentSerializer
from rest_framework import status


# Homepage
def homepage(request):
    students = StudentDetail.objects.all()

    return render(request, "homepage.html", {
        "students": students
    })


# Add Student
def add_student(request):

    if request.method == "POST":
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("homepage")

    else:
        form = StudentForm()

    return render(request, "add_student.html", {
        "form": form
    })


# View Student Details
def details(request, id):

    student = get_object_or_404(StudentDetail, id=id)

    return render(request, "view_details.html", {
        "student": student
    })


# Update Student
def update_student(request, id):

    student = get_object_or_404(StudentDetail, id=id)

    if request.method == "POST":

        form = StudentForm(request.POST, instance=student)

        if form.is_valid():
            form.save()
            return redirect("homepage")

    else:
        form = StudentForm(instance=student)

    return render(request, "update.html", {
        "form": form
    })


# Delete Student
def delete_student(request, id):

    student = get_object_or_404(StudentDetail, id=id)
    student.delete()

    return redirect("homepage")


# API Views
class StudentListCreateAPI(APIView):

    def get(self, request):
        students = StudentDetail.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)

        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):

        student = get_object_or_404(StudentDetail, id=id)

        serializer = StudentSerializer(
            student,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_200_OK)

        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)