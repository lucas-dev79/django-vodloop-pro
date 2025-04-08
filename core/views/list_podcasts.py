from django.shortcuts import render
from core.models import Podcast
from django.contrib.auth.decorators import login_required

@login_required
def list_podcasts(request):
    podcasts = Podcast.objects.all()

    for podcast in podcasts:
        print(f"Podcast: {podcast.title}, Slug: {podcast.slug}")

    return render(request, "list_podcasts.html", context={"podcasts": podcasts})
