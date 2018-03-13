from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy

from dimagi.pages.models.commcare import (
    FeatureGroup,
    Feature,
    Support,
)


GROUP = FeatureGroup(
    title=ugettext_lazy(
        "User management"
    ),
    slug='user-management',
)

GROUP.add_features([
    Feature(
        title=ugettext_lazy(
            "User groups"
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
            "Case sharing"
        ),
        description=ugettext_lazy(
            "Being able to share data across users."
        ),
        support=Support(True, True, True, True),
    ),
    Feature(
        title=ugettext_lazy(
            "Role-based access"
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
            "Organization-based case sharing"
        ),
        description=ugettext_lazy(
            "For projects using case sharing between different groups of "
            "users, automatically manage case sharing privileges based on "
            "your organization’s hierarchy. Create an organization chart that "
            "represents your organizational hierarchy and add mobile "
            "workers to different working groups or locations."
        ),
        support=Support(True, True, True, True),
    ),
    Feature(
        title=ugettext_lazy(
            "Organization-based data export and user management restrictions"
        ),
        description=ugettext_lazy(
            "For projects using the the organization hierarchy, restricts "
            "the data exports and ability to edit mobile workers based on "
            "which part of the organization chart a web user is assigned to."
        ),
        support=Support(False, True, True, True),
    ),
])
