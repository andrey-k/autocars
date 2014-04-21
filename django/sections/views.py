from django.shortcuts import render
from django.shortcuts import get_list_or_404

from django.views.decorators.http import require_POST

from sections.models import SpecialOffer
from sections.models import Service
from sections.models import Testimonial
from sections.models import Worker
from sections.forms import ContactForm


def index(request):
    week_offer = SpecialOffer.objects.filter(
        is_active=True, is_week_offer=True).first()
    special_offers = SpecialOffer.objects.filter(
        is_active=True, is_week_offer=False)[:3]

    services = Service.objects.all()

    testimonials = Testimonial.objects.all()

    workers = Worker.objects.all()

    form = ContactForm(label_suffix='')

    return render(request, 'sections/index.html',
                  {'week_offer': week_offer, 'special_offers': special_offers,
                   'services': services, 'testimonials': testimonials,
                   'workers': workers, 'form': form})


@require_POST
def contact(request):
    print('contact')

    return render(request, 'sections/index.html', {})
