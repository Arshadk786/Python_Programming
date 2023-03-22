
from django.shortcuts import render,HttpResponse
from Home.models import Contact
from django.contrib import messages


# Create your views here.
def index(request):
    context = {
        'a': '50'
    }
    # return HttpResponse("This is a Home Page")
    return render(request,'index.html',context)

def services(request):
    return render(request, 'service.html')

def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        contact = Contact(name=name,email=email,phone=phone,message=message)
        contact.save()
        messages.success(request, 'Form Submitted Successfully!!')
    return render(request, 'contact.html')
    