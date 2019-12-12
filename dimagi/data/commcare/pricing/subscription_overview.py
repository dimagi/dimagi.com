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
        support=Support("1", "1", "1", "1"),
    ),
    Feature(
        title=ugettext_lazy(
            "# of Web Users"
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
            "# of Form Submissions"
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
