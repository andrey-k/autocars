from django.shortcuts import render
from django.shortcuts import get_list_or_404

from sections.models import SpecialOffer
from sections.models import Service
from sections.models import Testimonial


def index(request):
    week_offer = SpecialOffer.objects.filter(
        is_active=True, is_week_offer=True).first()
    special_offers = SpecialOffer.objects.filter(
        is_active=True, is_week_offer=False)[:3]

    services = Service.objects.all()

    testimonials = Testimonial.objects.all()

    return render(request, 'sections/index.html',
                  {'week_offer': week_offer, 'special_offers': special_offers,
                   'services': services, 'testimonials': testimonials})
