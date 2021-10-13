from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy

from dimagi.pages.models.commcare import (
    FeatureGroup,
    Feature,
    Support,
)


GROUP = FeatureGroup(
    title=ugettext_lazy(
        "Enterprise Management Tools"
    ),
    slug='enterprise-management-tools',
)

GROUP.add_features([
    Feature(
        title=ugettext_lazy(
            "Enterprise Release Management"
        ),
        description=ugettext_lazy(
            "The safe and simple way to deploy standardised M&E or "
            "service delivery solutions to country teams. ERM allows "
            "organisations to build apps and configurations on an upstream "
            "project space and then push them to many downstream project "
            "spaces. Ideal for software development risk mitigation and rapid "
            "deployment to multiple local teams."
        ),
        support=Support(False, False, False, True),
    ),
    Feature(
        title=ugettext_lazy(
            "Single Sign-On"
        ),
        description=ugettext_lazy(
            "Adhere to internal access control policies with enterprise-grade "
            "security. Essential for global organisations that require regulatory "
            "compliance and tight administration of identity access."
        ),
        support=Support(False, False, False, True),
    ),
    Feature(
        title=ugettext_lazy(
            "The Enterprise Console"
        ),
        description=ugettext_lazy(
            "Administer CommCare globally with ease. Evaluate CommCare usage across "
            "regions, manage billing centrally, standardise reporting across project "
            "spaces, and access enterprise settings."
        ),
        support=Support(False, False, False, True),
    ),
    
])
