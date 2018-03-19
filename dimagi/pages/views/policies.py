from django.shortcuts import render
from django.utils.translation import ugettext


def privacy(request):
    return render(request, 'pages/policies.html', {
        'policy': 'sections/policies/privacy.html',
        'policy_title': ugettext("Privacy Policy"),
    })


def eula(request):
    return render(request, 'pages/policies.html', {
        'policy': 'sections/policies/eula.html',
        'policy_title': ugettext("End User License Agreement"),
    })


def subscription(request):
    return render(request, 'pages/policies.html', {
        'policy': 'sections/policies/subscription.html',
        'policy_title': ugettext("Product Subscription Agreement"),
    })
