from django.shortcuts import render, get_object_or_404
from core.models import Podcast
from django.contrib.auth.decorators import login_required

@login_required
def podcast_detail(request, slug):
    podcast = get_object_or_404(Podcast, slug=slug)
    
    context = {"podcast": podcast}
    return render(request, "podcast_detail.html", context)

    
