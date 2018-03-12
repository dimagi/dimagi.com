from django.shortcuts import render
from dimagi.utils.decorators import no_index


@no_index
def privacy(request):
    return render(request, 'pages/policies.html', {
        'policy': 'sections/policies/privacy.html',
    })


@no_index
def eula(request):
    return render(request, 'pages/policies.html', {
        'policy': 'sections/policies/eula.html',
    })


@no_index
def subscription(request):
    return render(request, 'pages/policies.html', {
        'policy': 'sections/policies/subscription.html',
    })
