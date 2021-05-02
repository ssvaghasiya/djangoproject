from django.shortcuts import render

# Create your views here.


def show_details(request, my_id):
    return render(request, 'enroll/show.html',{'id':my_id})

def home(request,check):
    print(check)
    return render(request, 'enroll/home.html')

def show_subdetails(request, year):
    return render(request, 'enroll/show.html',{'year':year})