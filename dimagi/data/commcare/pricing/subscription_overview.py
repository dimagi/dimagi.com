from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy

from dimagi.pages.models.commcare import (
    FeatureGroup,
    Feature,
    Support,
)


GROUP = FeatureGroup(
    title=ugettext_lazy(
        "Subscription Overview"
    ),
    slug='subscription-overview',
)

GROUP.add_features([
    Feature(
        title=ugettext_lazy(
            "# of Project Spaces"
        ),
        description=ugettext_lazy(
            "A CommCare project space is the web-based portal where you "
            "manage users, CommCare mobile applications, data, settings, and "
            "more. Data is not shared among project spaces; only people you "
            "invite to your project space will be able to see your "
            "application or your data."
        ),
        support=Support("1", "1", "1", "Custom"),
    ),
    Feature(
        title=ugettext_lazy(
            "# of Web Users"
        ),
        description=mark_safe(ugettext_lazy("""All CommCare subscription plans include unlimited 
    <a href="https://confluence.dimagi.com/display/commcarepublic/CommCare+Fundamentals+-+Web+and+Mobile+Users#"
    target="_blank">web users</a>.
        """)),
        support=Support(
            standard=ugettext_lazy(
                "Unlimited"
            ),
            pro=ugettext_lazy(
                "Unlimited"
            ),
            advanced=ugettext_lazy(
                "Unlimited"
            ),
            enterprise=ugettext_lazy(
                "Unlimited"
            ),
        ),
    ),
    Feature(
        title=ugettext_lazy(
            "# of Form Submissions"
        ),
        description=ugettext_lazy(
            "All CommCare subscription plans include unlimited form submissions."
        ),
        support=Support(
            standard=ugettext_lazy(
                "Unlimited"
            ),
            pro=ugettext_lazy(
                "Unlimited"
            ),
            advanced=ugettext_lazy(
                "Unlimited"
            ),
            enterprise=ugettext_lazy(
                "Unlimited"
            ),
        ),
    ),
    Feature(
        title=ugettext_lazy(
            "Data storage"
        ),
        description=ugettext_lazy(
            "All CommCare subscription plans provide unlimited data "
            "storage, including unlimited storage for data collected in form "
            "submission as well as all application data."
        ),
        support=Support(
            standard=ugettext_lazy(
                "Unlimited"
            ),
            pro=ugettext_lazy(
                "Unlimited"
            ),
            advanced=ugettext_lazy(
                "Unlimited"
            ),
            enterprise=ugettext_lazy(
                "Unlimited"
            ),
        ),
    ),
])
