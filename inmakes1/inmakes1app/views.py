from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def detail(request):
    return render(request,'detail.html')

def thanks(request):
    return HttpResponse('Thankyou for visiting our page:)')

def passingvalue(request):
    name='india'
    return render(request,'passingvalue.html',{'obj':name})

def page1(request):

    return render(request,'page1.html')

def resultpage(request):
     x = int(request.GET['num1'])
     y = int(request.GET['num2'])
     add = x+y
     minus=x-y
     mult=x*y
     div=x/y
     return render(request,'resultpage.html',{'addresult':add,'minusresult':minus,'multresult':mult,'divresult':div})

