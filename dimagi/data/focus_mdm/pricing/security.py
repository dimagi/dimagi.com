from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy

from dimagi.pages.models.focus_mdm import (
    FeatureGroup,
    Feature,
    Support,
)


GROUP = FeatureGroup(
    title=ugettext_lazy(
        "Security management"
    ),
    slug='security',
)

GROUP.add_features([
    Feature(
        title=ugettext_lazy(
            "Two-factor authentication"
        ),
        description=ugettext_lazy(
            "Turn on two-factor authentication for your web user to add a "
            "second level of authentication and make your account more secure. "
        ),
        support=Support(False, False, True, True),
    ),
    Feature(
        title=ugettext_lazy(
            "Remote wipe device"
        ),
        description=ugettext_lazy(
            "Enables IT admin to wipe device from afar. "
            "This action executes factory reset on a device. "
            "Once wiped, no data can be recovered from a device.  "
        ),
        support=Support(False, False, True, True),
    ),
    Feature(
        title=ugettext_lazy(
            "Remote device lock"
        ),
        description=ugettext_lazy(
            "Enables IT admin to lock device remotely by entering 6 digit passcode. "
            "Device can be unlocked either by entering passcode or remotely, "
            "by clicking on unlock button which is located on device page.  "
        ),
        support=Support(False, False, True, True),
    ),
    Feature(
        title=ugettext_lazy(
            "Device encryption"
        ),
        description=ugettext_lazy(
            "Encryption stores device's data in an unreadable,  "
            "seemingly scrambled form. It is being used as extra security measure "
            "by some organizations that work with sensitive data or have high security standards.  "
        ),
        support=Support(False, False, False, True),
    ),
])
