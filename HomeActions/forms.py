from django import forms
from django import forms
from django.db import models
from django import forms
from .models import CustomerResponse

class CustomerResponseForm(forms.ModelForm):
    class Meta:
        model=CustomerResponse
        fields=['name','email','whatsapp_number','details','is_interested']

    def __init__(self, *args, **kwargs):
        super(CustomerResponseForm,self).__init__(*args,**kwargs)
        #Charfields
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['whatsapp_number'].widget.attrs['class'] = 'form-control'

        #Textarea
        self.fields['details'].widget.attrs['class'] = 'form-control'
        self.fields['details'].widget.attrs['rows'] = '5'

        