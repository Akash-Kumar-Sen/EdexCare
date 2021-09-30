from django import forms
from django.shortcuts import render
from HomeActions.models import HomeActions
from events.models import Testimonial,Contact,Resource
from events.forms import ContactForm
from django.contrib import messages


def index(request):
    homeactions = HomeActions.objects.all().order_by('id')
    testimonials = Testimonial.objects.all().order_by('id')

    context={
        'homeactions' : homeactions,
        'testimonials' : testimonials,
    }
    return render(request,'home.html',context)


def aboutus(request):
    return render(request,'nav-links/aboutus.html',context={})

def resources(request):
    resources=Resource.objects.all().order_by('id')
    context={
        'resources':resources,
    }
    return render(request,'nav-links/resources.html',context)

def contactus(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            first_name=form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            email=form.cleaned_data['email']
            phone=form.cleaned_data['phone']
            message=form.cleaned_data['message']

            ContactObject = Contact.objects.create(
               first_name=first_name,
               last_name=last_name,
               email=email,
               phone=phone,
               message=message,
            )

            ContactObject.save()

            messages.success(request, 'Data Submitted Succesfully!')
        else:
            messages.error(request, 'Invalid Request, Please fill the form properly!')
    else:
        form=ContactForm()

    context={
        'form':form,
    }
    return render(request,'nav-links/contactus.html',context)