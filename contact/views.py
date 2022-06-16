from django.shortcuts import (
    render, redirect, reverse, get_object_or_404, HttpResponse)
from django.contrib import messages
from .forms import ContactForm
from .models import Contact_message


def error_403(request, exception):
    '''403 error view'''
    return render(request, '403.html', status=403)


def error_404(request, exception):
    '''
    A 404 error handling view
    '''
    return render(request, '404.html', status=404)


def error_500(request, *args, **argv):
    '''
    A 500 error handling view
    '''
    return render(request, '500.html', status=500)


def Contact(request):
    """
    A view to return the contact page
    """
    if request.method == 'POST':

        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.success(request, 'Message Sent!')
            return redirect(reverse('contact'))
        else:
            messages.error(request, 'Please check your form is valid.\
                Message send failed.')

    else:
        contact_form = ContactForm()

    template = 'contact/contact.html'

    context = {
        'contact_form': contact_form,
    }

    return render(request, template, context)
