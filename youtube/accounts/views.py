from django.shortcuts import render , redirect
from django.views.generic import CreateView 
from django.urls import reverse , reverse_lazy
from .forms import CustomCreationForm
from django.contrib.auth import login
# Create your views here.

class RegisterView(CreateView):
    success_url = reverse_lazy('accounts:login')
    form_class = CustomCreationForm
    template_name = 'accounts/register.html' 

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):

        response = super().form_valid(form)
        login(self.request , self.object)
        return response