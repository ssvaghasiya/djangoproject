from django.shortcuts import render
from .forms import StudentRegistration
from .models import User

# Create your views here.
def showfromdata(request):
    if request.method == 'POST':
        pi = User.object.get(pk=1) #pk = primary key using this update any entry
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            # print('Form Validated')
            # nm = fm.cleaned_data['name']
            # em = fm.cleaned_data['email'] 
            # pw = fm.cleaned_data['password']
            # reg = User(name=nm,email=em,password=pw)
            # reg.save()

    else: 
        fm = StudentRegistration()
    
    return render(request,'enroll/userregistration.html',{'form':fm})