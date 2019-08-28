from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy

from dimagi.pages.models.focus_mdm import (
    FeatureGroup,
    Feature,
    Support,
)


GROUP = FeatureGroup(
    title=ugettext_lazy(
        "Device management"
    ),
    slug='device-management',
)

GROUP.add_features([
    Feature(
        title=ugettext_lazy(
            "Configurations"
        ),
        description=ugettext_lazy(
            "Set Email account, WiFi configuration, VPN, Wallpaper. "
        ),
        support=Support(False, True, True, True),
    ),
    Feature(
        title=ugettext_lazy(
            "Web content filtering"
        ),
        description=ugettext_lazy(
            "Choose which website are available to device user. "
        ),
        support=Support(False, False, False, True),
    )
])
