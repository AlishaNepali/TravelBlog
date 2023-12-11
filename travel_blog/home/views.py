from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html') 


def about(request):
    return render(request,'about.html') 

def blogs(request):
    return render(request,'blogs.html') 

def team(request):
    return render(request,'team.html') 

def experience(request):
    return render(request,'experience.html') 

def travel(request):
    return render(request,'travel.html') 