from django.views.generic.edit import CreateView
from blog.models import Blog

class AuthorCreate(CreateView):
    model = Blog
    fields = ['title']
