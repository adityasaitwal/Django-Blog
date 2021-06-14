from django.shortcuts import render,redirect
from django.http import HttpResponse
from . forms import SignUpForm
from . models import blog
from . forms import blog_form 

# Create your views here.

def Home(request):
    return render(request,"home.html")

def SignUp(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(SignUpDone)
    else:
        form = SignUpForm()
    return render(request,"signup.html",{"form":form})

def SignUpDone(request):
    return HttpResponse("Welcome!, Your account is created, Please enter your Username and Password in Admin Panel to login into your account")

def Post(request):
    if request.method=="POST":
        form=blog_form(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect(Read)
    else:
        form=blog_form()
    return render(request,"post.html",{"form":form})           

def Read(request):
    read=blog.objects.all()
    return render(request,"read.html",{"read":read})

def Update(request,id):
    upd=blog.objects.get(id=id)
    update=blog_form(request.POST or None,request.FILES or None,instance=upd)
    if update.is_valid():
        update.save()
        return redirect(Read)
    return render(request,"update.html",{"update":update})    

def Delete(request,id):
    del_t=blog.objects.get(id=id)    
    del_t.delete()

    return redirect(Read)



