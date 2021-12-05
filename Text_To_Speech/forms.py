from django import forms
from django.forms import ModelForm
from .models import Register_in_Data


class Register_Form(ModelForm):

	class Meta:

		model=Register_in_Data
		fields= ('uname_register','email_register','pword_register','pwordconform')
		