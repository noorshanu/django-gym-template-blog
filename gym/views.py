from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from .models import Contact
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request,'gym/index.html')

def fitness(request):
    return render(request,'gym/fitness.html')



def service(request):
    return render(request,'gym/service.html')
    


def about(request):
    return render(request,'gym/about.html')



def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        msg = request.POST.get('msg')
      
        contact = Contact(name=name,email=email,phone=phone,msg=msg)
        contact.save()
        send_mail(
            'New massage from Fitness Club',
            name+"\n"+email+"\n"+msg+ "\n"+ phone,
            'noor.alam.619@gmail.com',
            ['noor.alam.619@gmail.com'],
            fail_silently=False,   
            )   
        return redirect('thank')
    else:
        return render(request,'gym/contact.html')



def thank(request):
    return render(request,'gym/thank.html')
    