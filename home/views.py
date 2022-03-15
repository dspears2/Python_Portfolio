from django.shortcuts import render, HttpResponse

# Create your views here.


def home(request):
    return HttpResponse("This is the data")


def paths(request):
    # displays all paths on the website
    # fetch all the data from the models

    context = {
        'heading': "django tutorial 1",
        'content': "this is the best tutorial on the plant"
    }
    return HttpResponse("This is a path view")
