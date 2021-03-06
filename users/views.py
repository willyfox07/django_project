
from django.urls import reverse_lazy
from django.views import generic
from blog.forms.CustomUser import CustomUserCreationForm


class SignupPageView(generic.CreateView):
    """CLass for displaying registration page"""
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
