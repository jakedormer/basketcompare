from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
from django.forms import ValidationError, ModelForm
from products.models import Project, Merchant
from django.core.exceptions import NON_FIELD_ERRORS
from django.forms.widgets import CheckboxSelectMultiple
from django.template.defaultfilters import mark_safe



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

    

class CreateProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'merchants', ]
        labels = {
            "name": "1. Project Name",
            "merchants": "2. Merchants To Compare"
        }
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "A user cannot have two projects with the same name.",
            }
        }
        widgets = {
            'merchants': CheckboxSelectMultiple(attrs={'class': 'no-bullets mb-2'})
        }

    def __init__(self, *args, **kwargs):
        super(CreateProjectForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['class'] = 'form-control mb-2'
        self.fields['merchants'].queryset = Merchant.objects.exclude(merchant="basket compare")
        





    # def clean(self):
    #     cleaned_data = self.cleaned_data
    #     if Project.objects.filter(name=cleaned_data['name']).exists():
    #         raise ValidationError(
    #               'A project with this Name already exists')

    #     # Always return cleaned_data
    #     return cleaned_data











  




