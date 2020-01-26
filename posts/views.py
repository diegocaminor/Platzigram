""" Posts view. """
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, ListView
from datetime import datetime

from posts.models import Post
from posts.forms import PostForm

"""posts = [
    {
        'title': 'Mont Blanc',
        'user': {
            'name': 'Yésica Cortés',
            'picture': 'https://picsum.photos/60/60/?image=1027'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/800/600?image=1036',
    },
    {
        'title': 'Via Láctea',
        'user': {
            'name': 'Christian Van der Henst',
            'picture': 'https://picsum.photos/60/60/?image=1005'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/800/800/?image=903',
    },
    {
        'title': 'Nuevo auditorio',
        'user': {
            'name': 'Uriel (thespianartist)',
            'picture': 'https://picsum.photos/60/60/?image=883'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/500/700/?image=1076',
    }
]"""

class PostsFeedViews(LoginRequiredMixin, ListView):
    """ Return all published posts."""
    template_name = 'posts/feed.html'
    model = Post
    ordering  = ('-created',)
    paginate_by = 30
    context_object_name = 'posts'


class PostDetailView(LoginRequiredMixin, DetailView):
    """Return post detail."""

    template_name = 'posts/detail.html'
    queryset = Post.objects.all()
    context_object_name = 'post'

class CreatePostView(LoginRequiredMixin, CreateView):
    """Create a new post."""

    template_name = 'posts/new.hTml'
    form_class = PostForm
    success_url = reverse_lazy('posts:feed')

    def get_context_data(self, **kwargs):
        """Add user and profile to context."""
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['profile'] = self.request.user.profile
        return context

# Create your views here.
"""@login_required
def listPosts(request):"""
""" List existing posts."""
"""posts = Post.objects.all().order_by('-created')
return render(request, 'posts/feed.html', {'posts': posts})}"""

#@login_required
#def createPost(request):
#""" Create new post view."""
#if request.method == "POST":
#form = PostForm(request.POST, request.FILES)
#if form.is_valid():
#form.save()
#return redirect('posts:feed')
#else:
#form = PostForm()
#return render(
#request,
#template_name='posts/new.html',
#context = {
#'form': form,
#'user': request.user,
#'profile': request.user.profile
#}
#)