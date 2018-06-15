from __future__ import absolute_import
from django.utils.translation import ugettext_lazy
from dimagi.pages.models.quick_start import QuickStartArea, QuickStartSection
from dimagi.data.quick_start import cards


SECTION_A = QuickStartSection(
    title=ugettext_lazy("Build a CommCare app"),
    cards=[
        cards.GET_STARTED,
        cards.BECOME_A_PRO,
        cards.REVIEW_APP,
        cards.CONTACT_SUPPORT,
    ]
)


SECTION_B = QuickStartSection(
    title=ugettext_lazy("Minimize the support burden of your apps"),
    cards=[
        cards.HELP_APP_BUILDERS,
        cards.TECH_SUPPORT,
        cards.TROUBLESHOOT_APPS,
        cards.COMMUNITY,
    ]
)


SECTION_C = QuickStartSection(
    title=ugettext_lazy("Meet diverse stakeholder needs"),
    cards=[
        cards.SEND_DATA,
        cards.COLLECT_DATA,
        cards.CONTROL_ACCESS,
        cards.ADD_ONS,
    ]
)


SECTION_D = QuickStartSection(
    title=ugettext_lazy("Manage a scalable data collection platform"),
    cards=[
        cards.BUILD_CUSTOM_INTEGRATIONS,
        cards.MANAGE_ALL_YOUR_DATA,
        cards.TRUST_YOUR_INFRASTRUCTURE,
        cards.MANAGE_YOUR_DEVICES,
    ]
)


AREA = QuickStartArea(
    title=ugettext_lazy("Implement a scalable data solution"),
    slug='ict',
    description=ugettext_lazy(
        "Learn how to use CommCare to provide a "
        "scalable data solution for your clients."
    ),
    sections=[
        SECTION_A,
        SECTION_B,
        SECTION_C,
        SECTION_D,
    ]
)
