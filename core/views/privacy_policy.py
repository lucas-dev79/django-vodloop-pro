from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def privacy_policy(request):

    
    return render(request, "privacy_policy.html")