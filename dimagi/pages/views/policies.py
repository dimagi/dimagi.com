from django.shortcuts import render
from django.utils.translation import ugettext

from dimagi.utils.decorators import no_index


@no_index
def privacy(request):
    return render(request, 'pages/policies.html', {
        'policy': 'sections/policies/privacy.html',
        'policy_title': ugettext("Privacy Policy"),
    })


@no_index
def eula(request):
    return render(request, 'pages/policies.html', {
        'policy': 'sections/policies/eula.html',
        'policy_title': ugettext("End User License Agreement"),
    })


@no_index
def subscription(request):
    return render(request, 'pages/policies.html', {
        'policy': 'sections/policies/subscription.html',
        'policy_title': ugettext("Product Subscription Agreement"),
    })
