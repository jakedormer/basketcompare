from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
from django.forms import ValidationError


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
        	'username',
			'email',
			'password1',
			'password2' 
			)

    email = forms.EmailField(label=_('Email'), required=True)


    def save(self, commit=True):
    	user = super(SignUpForm, self).save(commit=False)
    	user.email = self.cleaned_data['email']

    	if commit:
    		user.save()

    def __init__(self, *args, **kwargs):
    	super(SignUpForm, self).__init__(*args, **kwargs)

    	self.fields['username'].widget.attrs['class'] = 'd-flex justify content-center form-control w-100'
    	self.fields['email'].widget.attrs['class'] = 'form-control w-100'
    	self.fields['password1'].widget.attrs['class'] = 'form-control w-100'
    	self.fields['password2'].widget.attrs['class'] = 'form-control w-100'

    	for fieldname in ['username', 'password1', 'password2', 'email']:
        	self.fields[fieldname].help_text = None

    
class AddToFavouritesForm(forms.Form):
	bc_sku = forms.CharField(label="bc_sku")





  




