from django.db import models
from django.utils.text import slugify


class Books(models.Model):
    title = models.CharField(max_length=200, blank=True, unique=True)
    subtitle = models.CharField(max_length=200, blank=True, unique=True)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='books/images')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.PositiveIntegerField()
    author = models.CharField(max_length=50)
    isbn = models.CharField(max_length=13)
    language = models.CharField(max_length=50)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Books, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
    
