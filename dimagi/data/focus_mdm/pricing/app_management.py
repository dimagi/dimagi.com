from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy

from dimagi.pages.models.focus_mdm import (
    FeatureGroup,
    Feature,
    Support,
)


GROUP = FeatureGroup(
    title=ugettext_lazy(
        "App management"
    ),
    slug='app-management',
)

GROUP.add_features([
    Feature(
        title=ugettext_lazy(
            "Block applications"
        ),
        description=ugettext_lazy(
            "Block application or application group for a device, "
            "device group or across all enrolled devices "
        ),
        support=Support(False, True, True, True),
    ),
    Feature(
        title=ugettext_lazy(
            "Advanced app blocking"
        ),
        description=ugettext_lazy(
            "Block apps based on time (ie. block YouTube from 9am-5pm), "
            "based on data usage (ie. block YouTube after 1GB of data used) "
        ),
        support=Support(False, True, True, True),
    ),
    Feature(
        title=ugettext_lazy(
            "Blacklist applications"
        ),
        description=ugettext_lazy(
            "Block applications for all enrolled and yet to be enrolled devices."
        ),
        support=Support(False, True, True, True),
    ),
    Feature(
        title=ugettext_lazy(
            "Managed playstore"
        ),
        description=ugettext_lazy(
            "Allow only certain applications to be downloaded and installed, "
            "Update, install, uninstall apps on devices silently. "
        ),
        support=Support(False, False, False, True),
    )
])
