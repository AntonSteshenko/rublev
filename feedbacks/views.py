from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib import messages
from django.core.mail import mail_admins
from django.views.generic import CreateView

from .models import Feedback


# Create your views here.

class FeedbackView(CreateView):
    model = Feedback
    fields = '__all__'
    success_url = reverse_lazy('feedback')
    template_name = 'feedback.html'

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


def index(request):
    return render(request,'index.html')
