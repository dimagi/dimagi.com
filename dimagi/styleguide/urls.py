from django.conf.urls import url

from dimagi.styleguide.views import (
    home,
    sizes,
    grid,
    colors,
)


urlpatterns = [
    url(r'^$', home, name='styleguide'),
    url(r'^sizes/$', sizes, name='styleguide_sizes'),
    url(r'^grid/$', grid, name='styleguide_grid'),
    url(r'^colors/$', colors, name='styleguide_colors'),
]
