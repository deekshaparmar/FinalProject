from django.shortcuts import render, redirect

from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect

from About.models import Banner
from . import forms as contact_forms

# Create your views here.

def contact(request):
    if request.method == 'GET':
        form = contact_forms.Contact_form()
    else:
        form = contact_forms.Contact_form(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['Name']
            from_mail = form.cleaned_data['Email_Id']
            message = form.cleaned_data['yourmessage']
            try:
                send_mail(subject, message, from_mail, ['deekshaparmar11@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            return redirect('/')
    context = {
        'Banners': Banner.objects.all(),

        'form': form
    }

    return render(request, 'Contact/contact.html', context)


