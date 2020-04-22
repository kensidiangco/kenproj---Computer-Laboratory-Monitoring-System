from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ('Students','Date', 'course','ID_number')
    list_filter = ['date']
    search_fields = ['first_name', 'last_name']
admin.site.register(Student, StudentAdmin)