from django.shortcuts import render


def open_source_home(request):
    return render(request, 'pages/open_source/open_source_home.html')
