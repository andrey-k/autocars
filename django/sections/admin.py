from django.contrib import admin
from models import SpecialOffer
from models import Service
from models import Worker
from models import Testimonial


class SpecialOfferAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'is_week_offer')

admin.site.register(SpecialOffer, SpecialOfferAdmin)
admin.site.register(Service)
admin.site.register(Worker)
admin.site.register(Testimonial)
