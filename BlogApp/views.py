from django.shortcuts import render

from .models import Post
from django.views import generic

#class Postlist(generic.ListView):
#    queryset = Post.objects.filter(status=1).order_by('-created_on')
#    template_name = 'index.html'

class Postlist(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    context_object_name = 'post_list'  # Make sure this is set

    def get_queryset(self):
        # Debug: Print the queryset to the console
        queryset = super().get_queryset()
        print(queryset)
        return queryset

class DetailView(generic.DetailView):
    model = Post
    template_name= 'post_detail.html'
    context_object_name = 'post'

# Create your views here.
