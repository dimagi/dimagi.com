from django.utils.translation import ugettext_lazy

from dimagi.pages.models.commcare import (
    FeatureGroup,
    Feature,
    Support,
)


GROUP = FeatureGroup(
    title=ugettext_lazy(
        "App creation and management"
    ),
    slug='app-creation',
)

GROUP.add_features([
    Feature(
        title=ugettext_lazy(
            "CommCare App Builder"
        ),
        description=ugettext_lazy(
            "CommCare features a user-friendly application builder "
            "that allows anyone to create a CommCare application without "
            "programming expertise. The application builder enables "
            "complex branching logic and data validation. The intuitive "
            "drag-and-drop user interface enables non-technical users "
            "to build applications."
        ),
        support=Support(True, True, True, True),
    ),
    Feature(
        title=ugettext_lazy(
            "Application Exchange"
        ),
        description=ugettext_lazy(
            "As the first open-licensed “app store” for mobile health, "
            "CommCare Exchange enables people to share and access "
            "pre-built CommCare applications at no cost. The CommCare "
            "community adds new applications on a regular basis for "
            "multiple sectors."
        ),
        support=Support(True, True, True, True),
    ),
    Feature(
        title=ugettext_lazy(
            "Application Release Manager"
        ),
        description=ugettext_lazy(
            "Manage multiple versions of your application, and remotely "
            "deploy new versions."
        ),
        support=Support(True, True, True, True),
    ),
])
