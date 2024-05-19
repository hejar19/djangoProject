from django.contrib import admin
from .models import Students,Professeur,Timetable
# Register your models here.
admin.site.register(Students)
admin.site.register(Professeur)
admin.site.register(Timetable)