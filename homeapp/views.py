from django.shortcuts import render , HttpResponse
from datetime import datetime
from homeapp.models import Contact
from django.contrib import messages


# Create your views here.
def index(request):
    context_dict = {
        'variable':'hi runit is good'

    } 
    #return HttpResponse("home app page")
    messages.success(request,"Your index page")

    return render(request,'index.html',context_dict)
def about(request):
    #return HttpResponse("About page")
    return render(request,'about.html')
def service(request):
    return render(request,'service.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name,email=email, phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request,"Your details are saved")
    return render(request,'contact.html')
