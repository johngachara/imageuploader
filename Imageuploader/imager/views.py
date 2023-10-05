from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .forms import PostForm
from .models import gachara
# Create your views here.
class HomePageView(ListView):
    model = gachara
    template_name = 'home.html'
class CreatePostView(CreateView):
    model = gachara
    template_name = 'post.html'
    form_class = PostForm
    success_url = reverse_lazy('home')


