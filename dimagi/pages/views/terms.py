from django.shortcuts import render
from django.utils.translation import ugettext


def privacy(request):
    return render(request, 'pages/terms.html', {
        'policy': 'sections/terms/privacy.html',
        'policy_title': ugettext("Privacy Policy"),
    })


def privacy_new(request):
    return render(request, 'pages/terms.html', {
        'policy': 'sections/terms/latest/privacy.html',
        'policy_title': ugettext("Privacy Policy"),
    })


def eula(request):
    return render(request, 'pages/terms.html', {
        'policy': 'sections/terms/eula.html',
        'policy_title': ugettext("End User License Agreement"),
    })


def subscription(request):
    return render(request, 'pages/terms.html', {
        'policy': 'sections/terms/subscription.html',
        'policy_title': ugettext("Product Subscription Agreement"),
    })
