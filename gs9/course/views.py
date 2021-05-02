from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def course_one(request):
    course_name = {'cname':'React'}
    return render(request, 'courseone.html',context=course_name)

def course_two(request):
    return render(request, 'coursetwo.html',{'cname':"Kotlin"})