from django.db import models
from django.core.validators import FileExtensionValidator, RegexValidator, EmailValidator
from django.utils.text import slugify

ALLOWED_EXTENSIONS = ["flac", "ogg", "mp3", "wav"]


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True, editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Podcast(models.Model):
    title = models.CharField(
        verbose_name="Title",
        max_length=1000,
    )

    description = models.TextField(
        verbose_name="Description",
        max_length=10000,
    )

    slug = models.SlugField( # website.com/podcasts/about-django About Django
        verbose_name="Slug",
        max_length=1000,
        unique=True,
        editable=False,
    )

    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        verbose_name="Author",
    )

    file = models.FileField(
        verbose_name="Podcast File",
        upload_to="podcast_uploads",
        validators=[FileExtensionValidator(allowed_extensions=ALLOWED_EXTENSIONS)]
    )

    m3u8_url = models.URLField(
        verbose_name="M3U8 URL",
        max_length=2000,
        blank=True,
        null=True,
    )

    thumbnail = models.ImageField(
        verbose_name="Podcast Thumbnail",
        upload_to="podcast_thumbnails",
    )

    poster_image = models.ImageField(
        verbose_name="Poster",
        upload_to="posters",
        blank=True,
        null=True
    )  

    categories = models.ManyToManyField(
        Category,
        blank=True,
        verbose_name="Categories"
    )


    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Podcast, self).save(*args, **kwargs)
    
    def __str__(self):
        return f'{self.title} by {self.author.username}'
    
    @property
    def poster_url(self):
        if self.poster_image:
            return self.poster_image.url
        return '/media/posters/default_poster.jpg'  

    

class Contact(models.Model):
    name = models.CharField(
        verbose_name="Name",
        max_length=100
    )

    email = models.EmailField(
        verbose_name="Email",
        max_length=254,
        unique=True,  # Ensures emails are unique
        validators=[EmailValidator(message="Email non valida")]
    )

    phone = models.CharField(
        verbose_name="Phone",
        max_length=15,
        validators=[
            RegexValidator(r'^\+?\d{10,15}$', "Il numero deve essere valido (10–15 cifre)")
        ]
    )

    subject = models.CharField(
        verbose_name="Subject",
        max_length=200
    )

    message = models.TextField(
        verbose_name="Message",
        max_length=10000
    )

    def __str__(self):
        return self.name