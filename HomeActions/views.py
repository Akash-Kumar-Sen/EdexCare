from django.shortcuts import render,redirect
from .models import HomeActions,ActionBullet,CustomerResponse
from .forms import CustomerResponseForm
from django.contrib import messages

# Create your views here.
def actions(request,name_slug):
    action=HomeActions.objects.get(name_slug=name_slug)
    action_bullets=ActionBullet.objects.filter(Action=action)

    if request.method == 'POST':
        form = CustomerResponseForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            email=form.cleaned_data['email']
            whatsapp_number=form.cleaned_data['whatsapp_number']
            details=form.cleaned_data['details']
            is_interested=form.cleaned_data['is_interested']

            CustomerResponseObject = CustomerResponse.objects.create(
                name=name,
                email=email,
                whatsapp_number=whatsapp_number,
                details=details,
                is_interested=is_interested,
                service_required=action,
            )

            CustomerResponseObject.save()

            messages.success(request, 'Data Submitted Succesfully!')
        else:
            messages.error(request, 'Invalid Request, Please fill the form properly!')
    else:
        form=CustomerResponseForm()
    context={
        'action':action,
        'action_bullets':action_bullets,
        'form' : form,
    }
    return render(request, "HomeActions/action.html", context)