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
    title=ugettext_lazy("Understand your program's performance"),
    cards=[
        cards.EXPORT_DATA_FOR_ANALYSIS,
        cards.MONITOR_CHANGES_OVER_TIME,
        cards.AUTOMATE_YOUR_REPORTS,
        cards.MONITOR_YOUR_WORKFORCE,
    ]
)


SECTION_C = QuickStartSection(
    title=ugettext_lazy("Manage field worker activity"),
    cards=[
        cards.CUSTOMIZE_ACCESS,
        cards.SHARE_CASES,
        cards.TRIGGER_SMS_REMINDERS,
        cards.GUIDE_FIELD_WORKERS,
    ]
)


SECTION_D = QuickStartSection(
    title=ugettext_lazy("Expand your program's impact"),
    cards=[
        cards.MULTIMEDIA,
        cards.EMPOWER_WITH_DATA,
        cards.PERFORM_BACKGROUND_CALCULATIONS,
        cards.ELIMINATE_DUPLICATE_DATA,
        cards.AUTOMATE_YOUR_REFERRALS,
    ]
)


AREA = QuickStartArea(
    title=ugettext_lazy("Improve Your Service Delivery"),
    slug='service-delivery',
    sections=[
        SECTION_A,
        SECTION_B,
        SECTION_C,
        SECTION_D,
    ]
)
