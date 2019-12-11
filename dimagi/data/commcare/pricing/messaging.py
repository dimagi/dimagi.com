from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy

from dimagi.pages.models.commcare import (
    FeatureGroup,
    Feature,
    Support,
)


GROUP = FeatureGroup(
    title=ugettext_lazy(
        "Messaging "
    ),
    slug='messaging',
)

GROUP.add_features([
    Feature(
        title=ugettext_lazy(
            "One-way messaging "
        ),
        support=Support(True, True, True, True),
    ),
    Feature(
        title=ugettext_lazy(
            "Live SMS chat"
        ),
        support=Support(True, True, True, True),
    ),
    Feature(
        title=ugettext_lazy(
            "Access to our in-country gateways"
        ),
        support=Support(True, True, True, True),
    ),
    Feature(
        title=ugettext_lazy(
            "Android gateway setup"
        ),
        support=Support(True, True, True, True),
    ),
    Feature(
        title=ugettext_lazy(
            "Two-way messaging"
        ),
        support=Support(False, False, True, True),
    ),
    Feature(
        title=ugettext_lazy(
            "Support to connect new in-country gateways"
        ),
        support=Support(False, False, True, True),
    ),
])
