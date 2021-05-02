from django.urls import path
from . import views

urlpatterns = [
    path('course_one/', views.course_one),
    path('course_two/', views.course_two),
]