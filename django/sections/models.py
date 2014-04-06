from django.db import models
from tinymce.models import HTMLField


class SpecialOffer(models.Model):
    title = models.CharField(max_length=200)
    short_description = HTMLField()
    description = HTMLField()
    price = models.DecimalField(max_digits=5, decimal_places=0)
    is_active = models.BooleanField(default=True)
    is_week_offer = models.BooleanField(default=False)
    image = models.ImageField(null=False, upload_to='offers')

    def __unicode__(self):
        return "{0}: is active - {1}, is week offer - {2}".format(
            self.title, self.is_active, self.is_week_offer)


class Service(models.Model):
    name = models.CharField(max_length=70)
    description = models.TextField()
    icon = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name


class Worker(models.Model):
    name = models.CharField(max_length=70)
    job_description = models.TextField()
    photo = models.ImageField(null=False, upload_to='photo')

    def __unicode__(self):
        return self.name


class Testimonial(models.Model):
    text = models.TextField()
    author = models.CharField(max_length=70)

    def __unicode__(self):
        return self.author
