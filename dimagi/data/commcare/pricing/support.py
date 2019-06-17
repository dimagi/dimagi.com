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
            "community-supported forum, for questions related to using "
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
            "Guaranteed First Response Time"
        ),
        description=ugettext_lazy(
            "Dimagi support staff will triage  "
            "and provide the first response to your inquiry "
            "within the specified first response time."
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
            "Guaranteed Follow-up Time"
        ),
        description=ugettext_lazy(
            "Dimagi support staff will follow-up with each of your replies "
            "within the specified response time"
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
            "Support on CommCare Bugs"
        ),
        description=ugettext_lazy(
            ""
        ),
        support=Support(True, True, True, True),
    ),
    Feature(
        title=ugettext_lazy(
            'Response to "App-specific Questions"'
        ),
        description=ugettext_lazy(
            ""
        ),
        support=Support(False, True, True, True),
    ),
])
