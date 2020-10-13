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
        description=ugettext_lazy(
            "CommCare User Groups allows organizations to group their "
            "mobile workers into different groups. You can use groups to "
            "filter reports and set up data sharing between users."
        ),
        support=Support(True, True, True, True),
    ),
    Feature(
        title=ugettext_lazy(
            "Web user roles"
        ),
        description=ugettext_lazy(
            "Restrict web users from accessing certain data or features by "
            "assigning them permission levels. This includes restricting "
            "access to identifying data that would violate HIPAA or other "
            "privacy standards."
        ),
        support=Support(True, True, True, True),
    ),
    Feature(
        title=ugettext_lazy(
            "Bulk user upload"
        ),
        description=ugettext_lazy(
            "Create and update your mobile worker groups, usernames, "
            "passwords, and other information in bulk through an easy excel "
            "import/export tool."
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
        description=ugettext_lazy(
            "The number of mobile users you can have using your project without"
            "additional charge. The Community plan allows for 10 free "
            "mobile users."
        ),
        support=Support("125", "250", "500", "Unlimited / discounted"),
    ),
    Feature(
        title=ugettext_lazy(
            "Price per additional mobile user"
        ),
        description=ugettext_lazy(
            "The monthly charge for users that are created above the free "
            "Mobile User limit"
        ),
        support=Support("2 USD/month", "2 USD/month", "2 USD/month", "Unlimited / discounted"),
    ),
])
