from __future__ import absolute_import
from django.utils.translation import ugettext_lazy
from dimagi.sectors.models import Area


HEALTH = Area(
    name=ugettext_lazy(
        "Health"
    ),
    theme="purple-theme",
)

