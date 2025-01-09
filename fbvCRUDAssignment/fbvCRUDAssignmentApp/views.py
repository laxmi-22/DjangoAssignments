from django.shortcuts import render,redirect
from fbvCRUDAssignmentApp.models import Course
from fbvCRUDAssignmentApp.forms import COurseForm
# Create your views here.
def getCourses(request):
    courses=Course.objects.all()
    return render(request,'fbvCRUDAssignmentApp/index.html',{'courses':courses})

def createCourse(request):
    form=COurseForm()
    if request.method=="POST":
        form=COurseForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request,'fbvCRUDAssignmentApp/create.html',{'form':form})
    

def updateCourse(request,id):    
    course=Course.objects.get(id=id)
    form=COurseForm(instance=course)
    if request.method=="POST":        
        form=COurseForm(request.POST,instance=course)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'fbvCRUDAssignmentApp/update.html',{'form':form})

def deleteCourse(request,id):
    course=Course.objects.get(id=id)
    course.delete()
    return redirect('/')
