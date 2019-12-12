from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy

from dimagi.pages.models.commcare import (
    FeatureGroup,
    Feature,
    Support,
)


GROUP = FeatureGroup(
    title=ugettext_lazy(
        "Application features"
    ),
    slug='app-features',
)

GROUP.add_features([
    Feature(
        title=ugettext_lazy(
            "Surveys"
        ),
        description=ugettext_lazy(
            "Collect data via mobile surveys. CommCare supports dozens "
            "of question types, including text, multiple choice, numeric, "
            "media capture (image, audio, video, signature), and advanced "
            "questions (GPS, barcodes, android app callouts)."
        ),
        support=Support(True, True, True, True),
    ),
    Feature(
        title=ugettext_lazy(
            "Flexible decision support"
        ),
        support=Support(True, True, True, True),
    ),
    Feature(
        title=ugettext_lazy(
            "Multi-language support"
        ),
        support=Support(True, True, True, True),
    ),
    Feature(
        title=ugettext_lazy(
            "Multimedia"
        ),
        support=Support(True, True, True, True),
    ),
    Feature(
        title=ugettext_lazy(
            "User case management"
        ),
        support=Support(True, True, True, True),
    ),
    Feature(
        title=ugettext_lazy(
            "Lookup tables"
        ),
        support=Support(True, True, True, True),
    ),
    Feature(
        title=ugettext_lazy(
            "Web-based applications"
        ),
        support=Support(False, False, True, True),
    ),
    Feature(
        title=ugettext_lazy(
            "Custom branding"
        ),
        support=Support(False, False, True, True),
    ),
    Feature(
        title=ugettext_lazy(
            "Application profiles"
        ),
        support=Support(False, False, False, False),
    ),
])
