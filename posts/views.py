"""Posts views."""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Utilities
from datetime import datetime
# Django

posts = [
    {
        'title': 'Mont Blac',
        'user': {
            'name': 'Yesica Cortes',
            'picture': 'https://picsum.photos/200/200/?image=1027',
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/800/600?image=1036',
    },
    {
        'title': 'Via Lactea',
        'user': {
            'name': 'C, Vander',
            'picture': 'https://picsum.photos/200/200/?image=903',
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/800/800/?image=903',
    },
    {
        'title': 'Nuevo auditorio',
        'user': {
            'name': 'Thespianartist',
            'picture': 'https://picsum.photos/200/200/?image=1076',
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/500/700/?image=1076',
    }
]

@login_required
def list_posts(request):
    """ List existing posts."""
    return render(request, 'posts/feed.html', {'posts': posts})
