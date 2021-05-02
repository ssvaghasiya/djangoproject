from django.urls import path
from . import views

urlpatterns = [
    path('fees_one/', views.fees_one),
    path('fees_two/', views.fees_two),
]