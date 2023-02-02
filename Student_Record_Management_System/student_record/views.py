from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def index_view(request):
    data = student.objects.all()
    context = {
        'data' : data
    }    

    return render(request,'student_record/home.html',context)

def add_view(request):
    if request.method == 'POST':
        print(request.POST)
        nm = request.POST.get('name')
        rl = int(request.POST.get('roll'))
        mk = int(request.POST.get('marks'))

        s1 = student(Name = nm , Roll = rl , Marks = mk)
        s1.save()
        return redirect('/display/')

    return render(request,'student_record/add.html')

def display_view(request):
    data = student.objects.all()
    context = {
        'data' : data
    }    

    return render(request,'student_record/display.html',context)


def update_view(request,id):
        s1 = student.objects.get(pk = id)
        context={'data':s1}

        if request.method == 'POST':
            nm = request.POST.get('name')
            rl = int(request.POST.get('roll'))
            mk = int(request.POST.get('marks'))

            # s1 = student(Name = nm , Roll = rl , Marks = mk)
            s1.Name = nm
            s1.Roll = rl
            s1.Marks = mk
            s1.save()
            
            return redirect('/display/')

        return render(request,'student_record/update.html',context)

def delete_view(request,id):
    s1 = student.objects.get(pk = id)
    context={'data':s1}
    if request.method =='POST':
        s1.delete()
        return redirect('/display/')
    return render(request,'student_record/delete.html',context)
