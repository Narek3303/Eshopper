from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings
from .forms import *
from .models import *

def contact_view(request):
    if request.method == 'POST':
        url = request.META.get('HTTP_REFERER')
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            cd = form.cleaned_data
            subject = f"{cd['subject']}" \
                      f"{cd['name']}"
            message = f"Comment {cd['comment']}"
            send_mail(subject, message, settings.EMAIL_HOST_USER,
                      [cd['email']])
            return redirect(url)
    else:
        form = ContactUsForm()


    return render(request, 'contact/contact.html', {'form': form})


def contact_info(request):
    text_info = ContactInformation.objects.first()
    info = ContactInformation.objects.all()


    return render(request, 'contact/contact.html', {'text_info': text_info,
                                                    'info': info})