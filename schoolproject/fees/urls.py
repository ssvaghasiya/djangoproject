from django.urls import path
from . import views

urlpatterns = [
    path('learnfv/', views.learn_python),
]