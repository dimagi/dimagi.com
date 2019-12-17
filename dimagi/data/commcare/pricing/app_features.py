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
        description=ugettext_lazy(
            "Complex workflows have the ability to track people and other "
            "entities over time and can include complex branching logic and "
            "rules for parsing and responding to messages. Organizations that "
            "support frontline workers or stock tracking often need complex "
            "workflows as opposed to simple workflows (which normally just "
            "support data collection)."
        ),
        support=Support(True, True, True, True),
    ),
    Feature(
        title=ugettext_lazy(
            "Multi-language support"
        ),
        description=ugettext_lazy(
            "Switch between multiple languages in your application, including "
            "non-roman character languages. For faster translations, "
            "use the “bulk upload” feature."
        ),
        support=Support(True, True, True, True),
    ),
    Feature(
        title=ugettext_lazy(
            "Multimedia"
        ),
        description=mark_safe(ugettext_lazy("""CommCare applications can include 
    <a href="https://wiki.commcarehq.org/display/commcarepublic/Multimedia+in+CommCare"
    target="_blank">multimedia</a> such as images, audio, and video, 
    which can be used for counseling or to aid low-literate users.
        """)),
        support=Support(True, True, True, True),
    ),
    Feature(
        title=ugettext_lazy(
            "User case management"
        ),
        description=ugettext_lazy(
            "Track data about your mobile workers over time. You can use "
            "this data to drive workflows in your application, just like "
            "regular case data."
        ),
        support=Support(True, True, True, True),
    ),
    Feature(
        title=ugettext_lazy(
            "Lookup tables"
        ),
        description=mark_safe(ugettext_lazy("""Allow your mobile 
    applications to “look up” information from an external data set. 
    <a href="https://wiki.commcarehq.org/display/commcarepublic/Lookup+Tables"
    target="_blank">Lookup tables</a> are useful for when you want to 
    reference large amounts of information, such as Weight-for-Age Z Score 
    tables for nutrition projects or extensive geographical locations.
        """)),
        support=Support(True, True, True, True),
    ),
    Feature(
        title=ugettext_lazy(
            "Web-based applications"
        ),
        description=ugettext_lazy(
            "Deploy your application to the mobile phone or the web. Log "
            "in and use the application via your web browser."
        ),
        support=Support(False, False, True, True),
    ),
    Feature(
        title=ugettext_lazy(
            "Custom branding"
        ),
        description=ugettext_lazy(
            "Display your logo instead of the CommCareHQ logo both on your "
            "web project space and Android mobile applications."
        ),
        support=Support(False, False, True, True),
    ),
    Feature(
        title=ugettext_lazy(
            "Application profiles"
        ),
        description=mark_safe(ugettext_lazy("""Create region-specific 
    <a href="https://wiki.commcarehq.org/display/commcarepublic/Application+Profiles"
    target="_blank">application profiles</a> that only install specific 
    languages and multimedia to a phone.  These reduce the installation size for 
    applications that support a large number of languages or regions.  
        """)),
        support=Support(False, False, True, True),
    ),
])
