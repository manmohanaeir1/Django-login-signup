from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required  


@login_required
def home(request):
    return render(request, "home.html", {})
   
# Create your views here.

 
    

def authView(request):
    form = UserCreationForm()
    if request.method == "POST": 
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect("base:login")
    return render(request, "registration/signup.html", {"form": form})
    
