from django.utils.translation import ugettext_lazy

from dimagi.pages.models.commcare import (
    FeatureGroup,
    Feature,
    Support,
)


GROUP = FeatureGroup(
    title=ugettext_lazy(
        "Support"
    ),
    slug='support',
)

GROUP.add_features([
    Feature(
        title=ugettext_lazy(
            "Online Learning Resources"
        ),
        description=ugettext_lazy(
            "Everyone has access to the CommCare Help Site and the "
            "CommCare Users forum. The CommCare Help Site has helpful "
            "documentation and tutorials. CommCare Users is a "
            "community-supported foru, for questions related to using "
            "CommCare. CommCare users from all over the world ask "
            "questions and share information."
        ),
        support=Support(True, True, True, True),
    ),
    Feature(
        title=ugettext_lazy(
            "Direct Email Support"
        ),
        description=ugettext_lazy(
            "With direct email support, organizations have access to a "
            "direct email address to reach Dimagi staff for CommCare "
            "support."
        ),
        support=Support(True, True, True, True),
    ),
    Feature(
        title=ugettext_lazy(
            "Phone Support"
        ),
        description=ugettext_lazy(
            "In addition to reporting issues through our direct email "
            "support, you can call the Dimagi support line to report "
            "issues. Dimagi support staff will respond by email or over "
            "the phone within the guaranteed response time."
        ),
        support=Support(False, False, True, True),
    ),
    Feature(
        title=ugettext_lazy(
            "Guaranteed Response Time"
        ),
        description=ugettext_lazy(
            "Dimagi support staff will review any issues you report "
            "and contact you with a first response within the "
            "guaranteed response time."
        ),
        support=Support(
            standard=ugettext_lazy(
                "3 Business Days"
            ),
            pro=ugettext_lazy(
                "1 Business Day"
            ),
            advanced=ugettext_lazy(
                "1 Business Day"
            ),
            enterprise=ugettext_lazy(
                "1 Business Day"
            ),
        ),
    ),
])
