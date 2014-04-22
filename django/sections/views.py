import json

from django.core.mail import send_mail

from django.http import HttpResponseBadRequest
from django.http import HttpResponse

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
    response_data = {
        'status': 'FAIL',
        'messageClass': 'alert-danger',
        'message': None,
    }

    if request.is_ajax():
        form = ContactForm(request.POST)
        if form.is_valid():
            message = 'From: {name}({phone})<{email}>\r\n\r\n \
            Message:\r\n{message}\r\n'.format(
                name=form.cleaned_data['name'],
                phone=form.cleaned_data['telephone_number'],
                email=form.cleaned_data['email_address'],
                message=form.cleaned_data['message']
            )
            send_mail(form.cleaned_data['subject'], message,
                      'andrey.kramarev@gmail.com',
                      ['andrey.kramarev@gmail.com'])
            response_data['status'] = 'OK'
            response_data['messageClass'] = 'alert-success'
            response_data['message'] = 'Message sent. \
                                        Thank you for you message.'
        else:
            if form.errors:
                response_data['message'] = 'Couldn\'t send mail. \
                                            Check entered data.'

    return HttpResponse(json.dumps(response_data),
                        content_type='application/json')
