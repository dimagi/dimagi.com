from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy

from dimagi.pages.models.focus_mdm import (
    FeatureGroup,
    Feature,
    Support,
)


GROUP = FeatureGroup(
    title=ugettext_lazy(
        "Groups"
    ),
    slug='groups',
)

GROUP.add_features([
    Feature(
        title=ugettext_lazy(
            "Device groups"
        ),
        description=ugettext_lazy(
            "FocusMDM Device Groups allows organizations to group their "
            "devices into different groups. You can enforce "
            "policies on group, enroll devices directly into group."
        ),
        support=Support(False, True, True, True),
    ),
    Feature(
        title=ugettext_lazy(
            "Set policies per group"
        ),
        description=ugettext_lazy(
            "A policy can be assigned to a single device or device group."
        ),
        support=Support(False, True, True, True),
    ),
    Feature(
        title=ugettext_lazy(
            "Enroll devices directly into group"
        ),
        description=ugettext_lazy(
            "By sending enroll instructions with 'enroll in group' link. "
            "You can also bulk enroll devices into group. "
        ),
        support=Support(False, True, True, True),
    )
])
