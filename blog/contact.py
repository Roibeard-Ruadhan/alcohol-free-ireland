from django import forms
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect


class ContactForm(forms.Form):
    full_name = forms.CharField(max_length=100, label='Your Name')
    email = forms.EmailField(required=False, label='Your Email Address')
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)

# def contact(request):
#     submitted = False
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
            
#             # assert False
#             return redirect("home")
#     else:
#         form = ContactForm()
#         if 'submitted' in request.GET:
#             submitted = True
 
#     return render(request, 
#         'contact/contact.html', 
#         {'form': form, 'submitted': submitted}
#         )