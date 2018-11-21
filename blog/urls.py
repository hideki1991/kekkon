from django.urls import path
from blog.views import BlogListView,BlogCreateView,\
BlogUpdateView,BlogDeleteView,BlogDetailView
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list'),
    path('detail/<pk>', BlogDetailView.as_view(), name='blog_detail'),
    path('create/', login_required(BlogCreateView.as_view()), name='blog_create'),
    path('update/<pk>', login_required(BlogUpdateView.as_view()), name='blog_update'),
    path('delete/<pk>', login_required(BlogDeleteView.as_view()), name='blog_delete')

]
