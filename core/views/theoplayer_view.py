from django.shortcuts import render

def theoplayer_view(request):
    # Retrieve video_url and poster_url from query parameters
    video_url = request.GET.get('video_url', '')
    poster_url = request.GET.get('poster_url', '')

    context = {
        'video_url': video_url,
        'poster_url': poster_url,
    }

    return render(request, 'player.html', context)