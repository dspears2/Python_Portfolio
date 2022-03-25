import email
from django.shortcuts import render, HttpResponse
from home.models import Contact

# Create your views here.


def index(request):
    #return HttpResponse("This is my homepage ")
    context = {'name':"harry",'course': "Django"}
    return render(request,'index.html',context)


def about(request):
    #return HttpResponse("This is my about page ")
    return render(request,'about.html')


def projects(request):
    #return HttpResponse("This is my projects page ")
    return render(request,'projects.html')


def contact(request):
    #return HttpResponse("This is my contact me page")
    if request.method== "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        contact = Contact(name=name,email=email,message=message) 
        contact.save()
        print("The data has been written to the database")
    return render(request,'contact.html')
