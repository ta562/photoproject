from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import CustomUser
from django.http import JsonResponse
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "signup.html"
    success_url = reverse_lazy('accounts:signup_success')
    def form_valid(self,form):
        user=form.save()
        self.object=user
        return super().form_valid(form)
class SignUpSuccessView(TemplateView):
    template_name="signup_success.html"

class CreateDeleteStudentsView(LoginRequiredMixin,TemplateView):
     template_name='createdeletestudents.html'

def ajax_get_userlist(request):
        text=request.GET.get('pk')
        userlist=list(CustomUser.objects.values_list('username',flat=True))
        useridlist=list(CustomUser.objects.values_list('id',flat=True))
        data ={'userlist':userlist,'useridlist':useridlist}
        return JsonResponse(data)

