"""Posts views."""

# from django.contrib.auth.decorators import login_required
#from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, ListView

# Forms
from posts.forms import PostForm

# Models
from posts.models import Post


class PostsFeedView(LoginRequiredMixin, ListView):
    """Return all published posts."""

    template_name = 'posts/feed.html'
    model = Post
    ordering = ('-created')
    paginate_by = 30
    context_object_name = 'posts'



class PostDetailView(LoginRequiredMixin, DetailView):
    """Return post detail."""

    template_name = 'posts/detail.html'
    queryset = Post.objects.all()
    context_object_name = 'post'

class CreatePostView(LoginRequiredMixin, CreateView):
    """Create new post view ."""

    template_name = 'posts/new.html'
    form_class = PostForm
    # reverse_lazy evalua la url hasta que la necesita
    succes_url = reverse_lazy('posts:feed')

    def get_context_data(self, **kwargs):
        """Add user and profile to context."""
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['profile'] = self.request.user.profile
        return context


# trabaja junto con LOGIN_URL en settings
# este decorador permite que no puedas entrar a post sin estar
# previamente logueado
def list_posts(request):
    """ List existing posts."""
    # -create con el signo de menos nos trae desde el ultimo creado
    posts = Post.objects.all().order_by('-created')
    return render(request, 'posts/feed.html', {'posts': posts})

#  sustituida por la clase create
# def create_post(request):
#     """Create new post view."""
#     if request.method == 'POST':
#         form = PostForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('posts:feed')
#     else:
#         form = PostForm()
#
#     return render(
#         request=request,
#         template_name='posts/new.html',
#         context={
#             'form': form,
#             'user': request.user,
#             'profile': request.user.profile,
#             }
#         )
