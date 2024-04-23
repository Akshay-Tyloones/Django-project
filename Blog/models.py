from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver

class BlogCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    categories = models.ManyToManyField(BlogCategory)
    slug = models.SlugField(max_length=200, unique=True, blank=True)

    def __str__(self):
        return self.title

    def total_viewed(self):
        return self.blogevent_set.filter(event_type='Viewed').count()

    def total_liked(self):
        return self.blogevent_set.filter(event_type='Liked').count()

    def total_shared(self):
        return self.blogevent_set.filter(event_type='Shared').count()

class BlogEvent(models.Model):
    EVENT_TYPES = (
        ('Viewed', 'Viewed'),
        ('Liked', 'Liked'),
        ('Shared', 'Shared'),
    )
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    event_type = models.CharField(max_length=20, choices=EVENT_TYPES)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self) -> str:
        return f"{self.blog} - {self.event_type}"


@receiver(pre_save, sender=Blog)
def generate_blog_slug(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)

@receiver(pre_save, sender=BlogCategory)
def generate_category_slug(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.name)