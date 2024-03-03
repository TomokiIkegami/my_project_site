from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import FormView

from .forms import ContactForm

from django.shortcuts import render, redirect, reverse
from django.views import View


class ContactFormView(FormView):
    template_name = 'contact/contact_form.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact_result')

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)
    
class ContactResultView(TemplateView):
    template_name = 'contact/contact_result.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['success'] = "Your message has been sent successfully."
        return context
        
    
    
class index(View):
    def get(self, request, *args, **kwargs):
        # return redirect(reverse('proj_overview:top_page'))
        return render(request,'top_page.html')  # return top page template directly

index = index.as_view()