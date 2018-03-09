from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy

from dimagi.pages.models.commcare import (
    FeatureGroup,
    Feature,
    Support,
)


GROUP = FeatureGroup(
    title=ugettext_lazy(
        "System integration"
    ),
    slug='integration',
)

GROUP.add_features([
    Feature(
        title=ugettext_lazy(
            "Data synchronization"
        ),
        description=mark_safe(ugettext_lazy("""For projects that want to 
        maintain their own in-house SQL database, use our 
        <a href="https://wiki.commcarehq.org/display/commcarepublic/CommCare+Data+Export+Tool"
           target="_blank">CommCare Data Export Tool</a>
       to sync CommCare data to your server.
        """)),
        support=Support(True, True, True, True),
    ),
    Feature(
        title=ugettext_lazy(
            "Zapier integration"
        ),
        support=Support(True, True, True, True),
    ),
    Feature(
        title=ugettext_lazy(
            "API access"
        ),
        description=ugettext_lazy(
            "CommCare supports access to Application Programming Interfaces "
            "(APIs). This allows organizations to configure CommCare so that "
            "all collected CommCare data can be integrated into external "
            "software programs."
        ),
        support=Support(True, True, True, True),
    ),
    Feature(
        title=ugettext_lazy(
            "Built-in integration (mobile apps, devices)"
        ),
        description=ugettext_lazy(
            "Access a set of built-in integrations between CommCare apps "
            "and a built-in 3rd party apps and devices."
        ),
        support=Support(False, True, True, True),
    ),
    Feature(
        title=ugettext_lazy(
            "External integration framework (mobile apps, devices)"
        ),
        description=ugettext_lazy(
            "Access to our integration framework that enables software "
            "developers to integrate CommCare apps with third party apps "
            "and devices."
        ),
        support=Support(False, False, True, True),
    ),
])
