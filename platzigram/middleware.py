"""Platzigram middleware catalog."""

# Django
from django.shortcuts import redirect
from django.urls import reverse

class ProfileCompletionMiddleware:
    """Profile completion middlewareself.

    Ensure every user that is interacting with the platform
    have their profile picture and biography.
    """

    def __init__(self, get_response):
        """Middleware initialization."""
        self.get_response = get_response

    def __call__(self, request):
        """Code to be executed for each request before the view is called."""
        if not request.user.is_anonymous:
            if not request.user.is_staff:
                # esta es una manera de traer los one2one
                profile = request.user.profile
                #import pdb; pdb.set_trace()
                if not profile.picture or not profile.biography:
                    if request.path not in [reverse('users:update'), reverse('users: logout')]:
                        return redirect('users:update')


        response = self.get_response(request)
        return response
