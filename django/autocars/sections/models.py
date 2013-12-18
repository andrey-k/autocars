from django.db import models
from tinymce.models import HTMLField

class SpecialOffer(models.Model):
    title = models.CharField(max_length=200)
    short_description = HTMLField()
    description = HTMLField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    is_active = models.BooleanField(default=True)
    is_week_offer = models.BooleanField(default=False)

    def __unicode__(self):
        return "{0}: is active - {1}, is week offer - {2}".format(
                self.title, self.is_active, self.is_week_offer)
