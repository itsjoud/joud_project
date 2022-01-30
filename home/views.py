from ast import Return
from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    #return HttpResponse("THIS IS OUR HOME PAGE")
    context = {'name': 'joud', 'course': 'django'}
    return render(request, 'home.html', context)

def about(request):
    #return HttpResponse("WE ARE A TECH COMPANY")
     return render(request, 'about.html')

def contact(request):   
    #return HttpResponse("this is our contact information")
     return render(request, 'contact.html')

def services(request):
    #return HttpResponse("these are our services")
    return render(request, 'services.html')


def updates(request):
    #return HttpResponse("this is our updates page")
    return render(request, 'updates.html')

