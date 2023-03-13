from django.urls import path
from app import views
from .views import CourseVedio

urlpatterns = [
    path('',views.index , name='index'),
    path('courses',views.course , name='course'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('team',views.team,name='team'),
    path('testimonial',views.testimonials,name='testimonial'),
    path('video',CourseVedio.as_view(),name='video'),
    path('signup',views.signup,name='signup'),
    path('signin',views.signin,name='signin'),
    path('logout',views.logout,name='logout'),
]