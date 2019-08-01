from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy

from dimagi.pages.models.focus_mdm import (
    FeatureGroup,
    Feature,
    Support,
)


GROUP = FeatureGroup(
    title=ugettext_lazy(
        "Location tracking"
    ),
    slug='location-tracking',
)

GROUP.add_features([
    Feature(
        title=ugettext_lazy(
            "Current Location of a Single Device on a map"
        ),
        description=ugettext_lazy(
            "IT admin has access to map which shows current location of a single device. "
            "This map is located on device page. "
        ),
        support=Support(True, True, True, True),
    ),
    Feature(
        title=ugettext_lazy(
            "Current Location of all devices"
        ),
        description=ugettext_lazy(
            "IT admin has access to map which shows current location of all devices. "
        ),
        support=Support(True, True, True, True),
    ),
    Feature(
        title=ugettext_lazy(
            "Last seen location of offline device"
        ),
        description=ugettext_lazy(
            "For offline devices you can track their last locations on a map. "
        ),
        support=Support(True, True, True, True),
    ),
    Feature(
        title=ugettext_lazy(
            "Heat map of area coverage"
        ),
        description=ugettext_lazy(
            "Heatmap shows covered area by your device users, "
            "For selected time period. "
            "You can specify some parameter values like point radius, "
            "choose radius measuring units. "
        ),
        support=Support(False, False, False, True),
    )
])
