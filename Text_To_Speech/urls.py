from django.urls import path,include
from Text_To_Speech import views

urlpatterns = [

    path('',views.home,name='home_page'),
    path('Register/',views.register,name='register_page'),
    path('Login/',views.login_function,name='login_page'),
    path('Speech/',views.speech_function,name='speech_page'),
    path('Speechrefresh',views.speech_refresh_form,name='speech_refresh_form'),
    path('Logout/',views.logout_function,name='logout_page')
    
    
]