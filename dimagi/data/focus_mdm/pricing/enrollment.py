from django.utils.translation import ugettext_lazy

from dimagi.pages.models.focus_mdm import (
    FeatureGroup,
    Feature,
    Support,
)


GROUP = FeatureGroup(
    title=ugettext_lazy(
        "Device enrollment"
    ),
    slug='device-enrollemnt',
)

GROUP.add_features([
    Feature(
        title=ugettext_lazy(
            "Email enrollment"
        ),
        description=ugettext_lazy(
            "Enroll device by sending enroll instructions to device user email."
        ),
        support=Support(True, True, True, True),
    ),
    Feature(
        title=ugettext_lazy(
            "SMS enrollment"
        ),
        description=ugettext_lazy(
            "Enroll device by sending enroll instructions to device user via SMS."

        ),
        support=Support(True, True, True, True),
    ),
    Feature(
        title=ugettext_lazy(
            "Bulk enrollment"
        ),
        description=ugettext_lazy(
            "Send multiple SMS, emails to device users at once."
        ),
        support=Support(True, True, True, True),
    ),
    Feature(
        title=ugettext_lazy(
            "Factory reset enrollment (DO mode)"
        ),
        description=ugettext_lazy(
            "Enroll device as company managed device."
        ),
        support=Support(False, False, False, True),
    ),
])
