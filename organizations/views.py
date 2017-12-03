from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.core.mail import mail_admins
from django.views.generic import CreateView, DetailView, TemplateView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.contrib.auth import logout

from feedbacks.models import Feedback
from .models import Organization
from offices.models import Office
from docs.models import Doc


# Create your views here.

class OrganizationMixin:
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['organization'] = Organization.objects.get(slug=self.args[0])
        return context

class IndexView(OrganizationMixin, TemplateView):
    template_name = 'organizations/index.html'
   
 

class FeedbackView(OrganizationMixin, CreateView):
    model = Feedback
    fields = '__all__'
    success_url = reverse_lazy('feedback')
    template_name = 'organizations/feedback.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Спасибо за ваше сообщение! Если вы оставили контактные данные мы свяжемся с вами.")
        try: 
            mail_admins(self.object.subject, self.object.message)
            print('ok')
        except:
            print('error')
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Обратная связь'
        return context

class DocListView(OrganizationMixin, ListView):
    model = Doc
    
    def get_queryset(self):
        return Doc.objects.filter(org_id=self.args[0]) 


class OfficeListView(OrganizationMixin, ListView):
    model = Office
    def get_queryset(self):
        return Office.objects.filter(org_id=self.args[0])

class OrgUpdateView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('organizations:login')
    model = Organization
    fields = '__all__'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['offices'] = Office.objects.filter(org_id = self.object.slug)
        context['docs'] = Doc.objects.filter(org_id = self.object.slug)
        return context  

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Изменения сохранены")
        return response

    def get_success_url(self):
        return reverse_lazy('organizations:admin', args=[self.object.slug])

   

class AdminLogoutView(LogoutView):
    
    def get_next_page(self):
        return reverse_lazy('organizations:index', args=[self.object.slug])

def logout_admin(request, pk):
    logout(request)
    return redirect('/mkk/' + pk + '/')


