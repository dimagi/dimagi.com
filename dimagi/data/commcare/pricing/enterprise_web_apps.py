from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy

from dimagi.pages.models.commcare import (
    FeatureGroup,
    Feature,
    Support,
)


GROUP = FeatureGroup(
    title=ugettext_lazy(
        "Enterprise Web Apps"
    ),
    slug='enterprise-web-apps',
)

GROUP.add_features([
    Feature(
        title=ugettext_lazy(
            "Price per Enterprise Web Apps user"
        ),
        description=ugettext_lazy(
            "The monthly charge for Enterprise Web Apps users."
        ),
        support=Support(False, False, False, "10 USD/month"),
    ),
    Feature(
        title=ugettext_lazy(
            "Web Apps optimized for complex case management use cases"
        ),
        description=ugettext_lazy(
            "Enterprise Web Apps are optimized to meet your most "
            "complex case management needs at scale."
        ),
        support=Support(False, False, False, True),
    ),
    Feature(
        title=ugettext_lazy(
            "One-click integration with AWS Connect"
        ),
        description=ugettext_lazy(
            "Launch Amazon's AWS Connect Dialer for call center workflows."
        ),
        support=Support(False, False, False, True),
    ),
    Feature(
        title=ugettext_lazy(
            "Automatic address capture using geocoder"
        ),
        description=ugettext_lazy(
            "Fully integrated geocoder question type to auto-capture addresses."
        ),
        support=Support(False, False, False, True),
    ),
    Feature(
        title=ugettext_lazy(
            "Cross-project space case transfers"
        ),
        description=ugettext_lazy(
            "Use cross-project space case transfers to drive powerful "
            "referral workflows across sites or geographies."
        ),
        support=Support(False, False, False, True),
    ),
    Feature(
        title=ugettext_lazy(
            "Custom one-click integrations with 3rd party systems"
        ),
        description=ugettext_lazy(
            "Our one-click integration framework allows users to "
            "launch 3rd party applications right from Web Apps."
        ),
        support=Support(False, False, False, True),
    ),
    
])
