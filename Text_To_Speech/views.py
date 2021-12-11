from django.shortcuts import render,redirect 
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,auth
import pyttsx3



# for function Creation


# Create your views here.

def home(request):

    return render(request,'Text_To_Speech/home.html')

def register(request):
    

    if request.method == 'POST':

        Username = request.POST['username']
        Email = request.POST['emailfield']
        Password = request.POST['password']
        confirm_password = request.POST['confirmpassword']
        
        if (Username == "" or Email == "" or Password == "" 

            or confirm_password == ""): 
            messages.warning(request,'Please Fill All The Field')
            return redirect('register_page')
        elif (len(Username) < 4):
            messages.warning(request,'Username Must Be Allowed More Than 4 Characters')
            return redirect('register_page')    
        elif (len(Password) < 8):
            messages.warning(request,'Password Must Be Allowed More Than 8 Characters')
            return redirect('register_page')
                
        else:

            if Password == confirm_password:

                if User.objects.filter(username=Username).exists():
                     messages.info(request,f'Username {Username} is Already Taken !!! ')
                     return redirect('register_page')

                elif User.objects.filter(email=Email).exists():  
                     messages.info(request,f'Email {Email} is Already Taken !!! ')
                     return redirect('register_page')
                else:
                    user=User.objects.create_user(username=Username,password=Password,email=Email)
                    user.save();
                    messages.info(request,f' hi {Username} Your Account Created SuccessFully , Please SignIn and Continue')
                    return redirect('home_page')
            else:
                 messages.error(request,'Password Not Match!!!')
                 return redirect('register_page')
    else:

        return render(request,'Text_To_Speech/Register_Page.html')


def login_function(request):

    if request.method == 'POST':
        username_or_email = request.POST['username']
        password = request.POST['password']
        
        
        user = auth.authenticate(request,username=username_or_email,password=password,)

        if username_or_email == "" or password == "":

            messages.warning(request,'Please Fill All The Field ')
            return redirect('login_page')
        else:

            if user is not None:

                    auth.login(request,user)

                    return redirect('speech_page')

            else:
                    messages.error(request,"Username or password is wrong")
                    return redirect('login_page')


    else:

         return render(request,'Text_To_Speech/Login_Page.html')

def logout_function(request):

    auth.logout(request)

    messages.success(request,'SuccessFully Logged out , Thanks for spending some quality time with the Web site today.')
    return redirect('home_page')






@login_required()
def speech_function(request):

    if request.method =='POST':

        text_speech=request.POST['speech_plaintext']

        if text_speech == "":

             messages.warning(request,'Please Type to Speech')
             return redirect('speech_page')

        else:
            def speech_ver():


                engine = pyttsx3.init()
                engine.say(text_speech)
                engine.runAndWait()
            # return HttpResponseRedirect('/Speech/')
            # messages.warning(request,"Something Wrong")
            return redirect('speech_page')



            
        #     # return HttpResponseRedirect('speech_page')
    else:           

        return render(request,'Text_To_Speech/Speech_Page.html',{'speech': speech_ver})




