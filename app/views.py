from django.shortcuts import render,redirect
from .models import Contact
from . models import Video
from .models import Signup
from . models import Courses
from django.views import View
from app.middlewares.auth import auth_middleware
from django.utils.decorators import method_decorator
from django.contrib.auth.hashers import make_password,check_password

# Create your views here.

def index(request):
    return render(request,'index.html')

def course(request):
    courses = Courses.objects.all()
    return render(request,'courses.html', {'courses':courses})

def about(request):
    return render(request,'about.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        contact = Contact(name = name,email=email,subject=subject,message=message)
        contact.save()
    return render(request,'contact.html')


def team(request):
    return render(request,'team.html')

def testimonials(request):
        return render(request,'testimonial.html')

class CourseVedio(View):
    @method_decorator(auth_middleware)
    def get(self,request):
        video = Video.objects.all()
        return render(request,'video.html',{"video":video})

def signup(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']

        #validation
        error_message = None
        if (not firstname):
            error_message = 'firstname required'
        elif len(firstname) <4:
            error_message = "firstname must be 4 char long"
        elif len(lastname) <4:
            error_message = "lastname must be 4 char long"
        elif len(email)<5:
            error_message = "email should be 5 char long"
        elif len(password) <10:
            error_message = "password must be 10 number long"
        
        if not error_message:
            user = Signup(firstname=firstname,lastname=lastname,phone=phone,email=email,password=password)
            user.password = make_password(user.password)
            user.save()
            return redirect('video')
        else:
            return render(request,'signup.html',{'error':error_message})
    else:
        return render(request,'signup.html')
    
def signin(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        password = request.POST['password']

        user = Signup.get_customer_by_firstname(firstname)
        print(user)
        error_message = None 
        if user:
            flag = check_password(password,user.password)
            if flag:
                request.session['user'] = user.id
                return redirect('video')
            
            else:
                error_message = 'email or password invalid'
        
            return render(request,'signin.html', {'error':error_message})

        
    return render(request,'signin.html')

def logout(request):
     request.session.clear()

     return redirect('index')
    


    