from django.shortcuts import render
from django.shortcuts import get_list_or_404

from autocars.sections.models import SpecialOffer


def index(request):
    offers = get_list_or_404(SpecialOffer)

    return render(request, 'sections/index.html', {'offers': offers})
