from django.contrib import admin
from .models import Contact,Video
from . models import Signup
from .models import Courses
from .models import Category
# Register your models here.


class AdminContact(admin.ModelAdmin):
    list_display = ['name','email','subject','message']

admin.site.register(Contact,AdminContact)


class AdminSignup(admin.ModelAdmin):
    list_display = ['firstname','lastname','email','phone','password']

admin.site.register(Signup,AdminSignup)


class AdminCourses(admin.ModelAdmin):
    list_display = ['course_name','price','description']

admin.site.register(Courses,AdminCourses)

class AdminCategory(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Category,AdminCategory)




admin.site.register(Video)


