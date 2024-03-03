from django import forms
from django.conf import settings
from django.core.mail import BadHeaderError, send_mail  # for sending mail
from django.http import HttpResponse

class ContactForm(forms.Form):
    subject = forms.CharField(
        label='',
        max_length=100,
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':"Subject",
        }),
    )
    name = forms.CharField(
        label='',
        max_length=100,
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':"Name",
        }),
    )
    email = forms.EmailField(
        label='',
        widget=forms.EmailInput(attrs={
            'class':'form-control',
            'placeholder':"Mail address",
        }),
    )
    message = forms.CharField(
        label='',
        widget = forms.Textarea(attrs={
            'class':'form-control',
            'placeholder':"Message",
        }),
    )
    def send_email(self):
        subject = self.cleaned_data['subject']
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        message = self.cleaned_data['message']+ '\n\n' + 'From: ' + name + '\n' + 'Email: ' + email
        from_email = '{name}<{email}>'.format(name=name,email=email)
        
        recipient_list = [settings.EMAIL_HOST_USER] # list of recipient
        try:
            send_mail(subject, message, from_email, recipient_list)
        except BadHeaderError:
            return HttpResponse('Invalid header found.')