from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy

from dimagi.pages.models.commcare import (
    FeatureGroup,
    Feature,
    Support,
)


GROUP = FeatureGroup(
    title=ugettext_lazy(
        "User Management"
    ),
    slug='user-management',
)

GROUP.add_features([
    Feature(
        title=ugettext_lazy(
            "Mobile user groups"
        ),
        support=Support(True, True, True, True),
    ),
    Feature(
        title=ugettext_lazy(
            "Web user roles"
        ),
        support=Support(True, True, True, True),
    ),
    Feature(
        title=ugettext_lazy(
            "Bulk user upload"
        ),
        support=Support(True, True, True, True),
    ),
    Feature(
        title=ugettext_lazy(
            "Locations-based web user roles"
        ),
        description=ugettext_lazy(
            "Organize web users according to the structure of your program "
            "to ensure admins can only view and access data submitted by "
            "mobile users in the group to which they've been assigned."
        ),
        support=Support(False, False, True, True),
    ),
    Feature(
        title=ugettext_lazy(
            "Included mobile users"
        ),
        support=Support("125", "250", "500", "Unlimited / discounted"),
    ),
    Feature(
        title=ugettext_lazy(
            "Price per additional mobile user"
        ),
        support=Support("2 USD/month", "2 USD/month", "2 USD/month", "Unlimited / discounted"),
    ),
])
