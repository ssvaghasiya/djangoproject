from . import views
from django.urls import path

urlpatterns = [
    path('formdata/', views.showfromdata),

]