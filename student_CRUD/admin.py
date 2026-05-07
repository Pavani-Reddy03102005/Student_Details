from django.contrib import admin
from .models import StudentDetail
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display=("name","email","course","enroll_date")
    search_fields=("name","email","course")
    list_filter=("course",)
admin.site.register(StudentDetail, StudentAdmin)