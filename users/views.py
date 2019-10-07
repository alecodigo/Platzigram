"""Users views."""

# Django
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, FormView, UpdateView

# Forms
from users.forms import  SignupForm

# Forms
from django.contrib.auth.models import User
from users.forms import Profile


class UserDetailView(LoginRequiredMixin, TemplateView):
    """User detail view."""

    template_name = 'users/detail.html'
    # los slug son campos de texto unicos
    slug_field = 'username'
    slug_url_kwarg = 'username'
    queryset = User.objects.all()
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        """Add user's posts to context."""
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['posts'] = Post.objects.filter(user=user).order_by('-created')
        return context

# lo sustituye la clase UpdateProfileView
# @login_required
# def update_profile(request):
#     """Update a user's profile view."""
#     profile = request.user.profile
#     if request.method == 'POST':
#         # los archivos viajan ej request.FILES
#         form = ProfileForm(request.POST, request.FILES)
#         if form.is_valid():
#             data = form.cleaned_data
#
#             profile.website = data['website']
#             profile.phone_number = data['phone_number']
#             profile.biography = data['biography']
#             profile.website = data['picture']
#             profile.save()
#
#             url = reverse('users:detail', kwargs={'username': request.user.username})
#             return redirect(url)
#     else:
#         form = ProfileForm()
#
#     return render(
#     request=request,
#     template_name='users/update_profile.html',
#     context={
#         'profile': profile,
#         'user': request.user,
#         'form': form,
#         }
#     )

class UpdateProfileView(LoginRequiredMixin, UpdateView):
    """Login view."""

    template_name = 'users/update_profile.html'
    model = Profile
    fields = ['website', 'biography', 'phone_number', 'picture']

    def get_object(self):
        """Return user's profile."""
        return self.requst.user.profile

    # trae una url absoluta
    def get_success_url(self):
        """Return to user's profile."""
        username = self.object.user.username
        return reverse('users:detail', kwargs={'username': username})

class LoginView(auth_views.LoginView):
    """Login view."""

    template_name = 'users/login.html'

#
# def login_view(request):
#     """Login view"""
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user:
#             login(request, user)
#             return redirect('posts:feed')
#         else:
#             return render(request, 'users/login.html', {'error': 'Invalid username or password'})
#     return render(request, 'users/login.html')
#

class SignupView(FormView):
    """Users sign up view."""

    template_name = 'users/signup.html'
    form_class = SignupForm
    succes_url = reverse_lazy('users:login')

    def form_valid(self, form):
        """Save form data."""
        form.save()
        return super().form_valid(form)

# reemplazo SignupView
# def signup(request):
#     """Sign up view."""
#     # import pdb; pdb.set_trace()
#     if request.method == 'POST':
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('users:login')
#     else:
#         form = SignupForm()
#
#     return render(
#         request=request,
#         template_name='users/signup.html',
#         context={'form': form}
#     )

# @login_required
# def logout_view(request):
#     """Logout a user."""
#     logout(request)
#     return redirect('users:login')


class LogoutView(auth_views.LoginView):
    """Logout view."""

    template_name = 'users/logged_out.html'
