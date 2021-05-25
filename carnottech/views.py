

from django.shortcuts import render
from . models import Students,Schools,Books



# Create your views here.
def home(request):
    
    return render(request,'home.html')

def student_details(request):
    #id=int(input("Enter an id:"))
    obj=Students.objects.get(id=1)
    obj2=Schools.objects.get(id=2)
    context={
        'Fullname': obj.First_name + ''+ obj.Last_name,
        'object' : obj,
        'object2': obj2
        }
    return render(request,'studentdetails/details.html',context)

def fetch(request):
    sid=int(request.GET['x'])
    name=request.GET['y']
    
    subj=Students.objects.get({'id':sid , 'First_name':name})
    context={
        'subject':subj
    }
    return render(request,'result.html',context)