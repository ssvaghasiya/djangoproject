from django.shortcuts import render
from .forms import StudentRegistration
# Create your views here.
def showfromdata(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        print(fm)
        print('Ye POST Request se aaya hai')
        if fm.is_valid:
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email'] 
            name1 = request.POST['name']
            print(fm.cleaned_data)
            print(name)
            print(email)
            print(name1)

    else: 
        fm = StudentRegistration()
        print('Ye Get Request se aaya hai')
    
    return render(request,'enroll/userregistration.html',{'form':fm})