from django.shortcuts import render
from core.models import Podcast
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    podcasts = Podcast.objects.all()[:3]
    return render(request, "index.html", context={"podcasts": podcasts})