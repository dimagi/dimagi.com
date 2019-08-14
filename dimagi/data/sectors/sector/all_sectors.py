from __future__ import absolute_import

from django.utils.translation import ugettext_lazy
from dimagi.pages.models.sectors import Sector


SECTOR = Sector(
    name=ugettext_lazy(
        "All"
    ),
    theme="turquoise",
    slug="all-sectors",
)
