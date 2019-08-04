from django.utils.translation import ugettext_lazy

from dimagi.pages.models.focus_mdm import (
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
            "Direct Email Support"
        ),
        description=ugettext_lazy(
            "With direct email support, organizations have access to a "
            "direct email address to reach Dimagi staff for FocusMDM. "
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
            basic=ugettext_lazy(
                "72 hours"
            ),
            standard=ugettext_lazy(
                "48 hours"
            ),
            advanced=ugettext_lazy(
                "24 hours"
            ),
            custom=ugettext_lazy(
                "12 hours"
            ),
        ),
    ),
    Feature(
        title=ugettext_lazy(
            "Support on FOCUSMDM Bugs"
        ),
        description=ugettext_lazy(
            "You can report a bug anytime by chatting with support staff "
            "via smooch chat bubble or by writing us on email address "
            "focus-support@dimagi.com"
        ),
        support=Support(True, True, True, True),
    ),
    Feature(
        title=ugettext_lazy(
            'Response to "App-specific Questions"'
        ),
        description=ugettext_lazy(
            "If you have any questions about our app features you "
            "can write to us via chat bubble or directly to support staff "
            "on focus-support@dimagi.com "
        ),
        support=Support(True, True, True, True),
    ),
])
