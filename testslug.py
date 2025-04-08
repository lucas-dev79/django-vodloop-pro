from core.models import Podcast
from django.utils.text import slugify

# Update slug for all podcasts with an empty slug
for podcast in Podcast.objects.filter(slug=""):
    podcast.slug = slugify(podcast.title)
    podcast.save()
    print(f"Updated Podcast: {podcast.title}, Slug: {podcast.slug}")

