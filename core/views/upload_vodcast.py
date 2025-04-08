from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from core.forms import PodcastForm

# Custom function to check if the user is a superuser
def is_superuser(user):
    return user.is_authenticated and user.is_superuser

# Restrict access only to superusers
@user_passes_test(is_superuser, login_url='/')  # Redirect non-superusers
@login_required
def upload_vodcast(request):
    if request.method == 'POST':
        form = PodcastForm(request.POST, request.FILES)
        if form.is_valid():
            podcast = form.save(commit=False)
            podcast.author = request.user
            podcast.save()
            form.save_m2m() 
            return redirect("home") #TODO
        
    else:
        form = PodcastForm()

    return render(request, "upload_vodcast.html", context={"form": form})