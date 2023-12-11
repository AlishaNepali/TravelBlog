from django.shortcuts import redirect, render
from authentication.forms import CreateUserform

# Create your views here.
def register(request):
    if request.method =="POST":
        form = CreateUserform(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username') 
            return redirect('home')
    else:
        form = CreateUserform()
    return render(request, 'register.html', {"form":form})