from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def fees_one(request):
    cname  = 'Django'
    duration = '4 Months'
    seats = 10
    django_details = {'nm':cname,'du':duration,'st':seats}
    return render(request, 'feesone.html',django_details)

def fees_two(request):
    return render(request, 'feestwo.html')