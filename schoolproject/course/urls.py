from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
    path('learndj/', views.learn_django),
    path('learnpy/', views.learn_python),
    path('learnv/', views.learn_var),
    path('learnm/', views.learn_math),
    path('learnf/', views.learn_format),
    path('', views.home,name='home'),

]