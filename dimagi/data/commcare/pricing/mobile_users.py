from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy

from dimagi.pages.models.commcare import (
    FeatureGroup,
    Feature,
    Support,
)


GROUP = FeatureGroup(
    title=ugettext_lazy(
        "Mobile users"
    ),
    slug='mobile-users',
)

GROUP.add_features([
    Feature(
        title=ugettext_lazy(
            "Free mobile user limit"
        ),
        description=ugettext_lazy(
            "The number of mobile users you can have using your project without"
            "additional charge. The Community plan allows for 10 free "
            "mobile users."
        ),
        support=Support("125", "250", "500", "Unlimited / discounted"),
    ),
    Feature(
        title=ugettext_lazy(
            "Price per additional mobile user"
        ),
        description=ugettext_lazy(
            "The monthly charge for users that are created above the free "
            "Mobile User limit"
        ),
        support=Support(
            "2 USD /month",
            "2 USD /month",
            "2 USD /month",
            "Unlimited / discounted"
        ),
    ),
])
