from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
  return render(request,'index.html')
def ind(request):
  return render(request,'hi.html')
def book(request):
  return render(request,'book.html')
def about(request):
    context = {}  # define an empty context dictionary
    return render(request, "about.html", context=context)
def menu(request):
    context = {}  # define an empty context dictionary
    return render(request, "menu.html", context=context)
def hello(request):
    context = {}  # define an empty context dictionary
    return render(request, "hello.html", context=context)
