from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy

from dimagi.pages.models.focus_mdm import (
    FeatureGroup,
    Feature,
    Support,
)


GROUP = FeatureGroup(
    title=ugettext_lazy(
        "Messaging & notifications"
    ),
    slug='messaging-notifications',
)

GROUP.add_features([
    Feature(
        title=ugettext_lazy(
            "Messaging (individual and group messaging)"
        ),
        description=ugettext_lazy(
            "Two-way messaging. IT admin can send one message to a device "
            "or device group. "
        ),
        support=Support(True, True, True, True),
    ),
    Feature(
        title=ugettext_lazy(
            "Notification center"
        ),
        description=ugettext_lazy(
            "Log into FocusMDM webapp and personalize your notification settings, i.e.  "
            "specify which issues/events are important to you. You will get "
            "notifications by email for all selected issues/events.  "
        ),
        support=Support(True, True, True, True),
    )
])
