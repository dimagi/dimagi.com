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
            "Online learning resources"
        ),
        support=Support(True, True, True, True),
    ),
    Feature(
        title=ugettext_lazy(
            "Direct email support"
        ),
        support=Support(True, True, True, True),
    ),
    Feature(
        title=ugettext_lazy(
            "Phone support"
        ),
        support=Support(False, False, True, True),
    ),
    Feature(
        title=ugettext_lazy(
            "Guaranteed first response time"
        ),
        support=Support(
            standard=ugettext_lazy(
                "3 business days"
            ),
            pro=ugettext_lazy(
                "1 business day"
            ),
            advanced=ugettext_lazy(
                "1 business day"
            ),
            enterprise=ugettext_lazy(
                "1 business day"
            ),
        ),
    ),
    Feature(
        title=ugettext_lazy(
            "Guaranteed follow-up time"
        ),
        support=Support(
            False,
            False,
            advanced=ugettext_lazy(
                "1 business day"
            ),
            enterprise=ugettext_lazy(
                "1 business day"
            ),
        ),
    ),
    Feature(
        title=ugettext_lazy(
            "Paid on-boarding"
        ),
        description=ugettext_lazy(
            "Dimagi's Customer Success team offers several onboarding "
            "options that provide hands-on assistance for designing, "
            "building, and implementing CommCare."
        ),
        support=Support(True, True, True, True),
    ),
    Feature(
        title=ugettext_lazy(
            'Access to our customer success team'
        ),
        description=ugettext_lazy(
            "Get regular, expert guidance from a dedicated Custom Success "
            "Manager for any issue—from debuggining to feature "
            "usage to application design."
        ),
        support=Support(False, False, False, True),
    ),
])
