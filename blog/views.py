from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from blog.models import Blog
from django.utils import timezone
from django.urls import reverse_lazy




# Create your views here.

class BlogListView(ListView):

    model = Blog
    paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class BlogDetailView(DetailView):

    model = Blog

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class BlogCreateView(CreateView):
    model = Blog
    success_url="/blog/"
    fields = ['title','text','category','document']
    login_required = True

class BlogUpdateView(UpdateView):
    model = Blog
    fields = ['title','text','category','document']
    template_name_suffix = '_update_form'
    success_url="/blog/"

class BlogDeleteView(DeleteView):
    model = Blog
    success_url = "/blog/"
