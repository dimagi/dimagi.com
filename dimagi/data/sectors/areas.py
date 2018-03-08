from __future__ import absolute_import
from django.utils.translation import ugettext_lazy
from dimagi.pages.models.sectors import Area


HEALTH = Area(
    name=ugettext_lazy(
        "Health"
    ),
    theme="purple-theme",
    icon="svg/products/commcare/icon/heart_health.html",
    css_class="sector-health",
)


DEVELOPMENT = Area(
    name=ugettext_lazy(
        "Development"
    ),
    theme="blue-theme",
    icon="svg/products/commcare/icon/retail.html",
    css_class="sector-development",
)


AGRICULTURE = Area(
    name=ugettext_lazy(
        "Agriculture"
    ),
    theme="green-theme",
    icon="svg/products/commcare/icon/agriculture.html",
    css_class="sector-agriculture",
)
