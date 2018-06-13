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
    title=ugettext_lazy("Create reports and dashboards"),
    cards=[
        cards.EXPORT_DATA_FOR_ANALYSIS,
        cards.MONITOR_CHANGES_OVER_TIME,
        cards.AUTOMATE_YOUR_REPORTS,
        cards.LINK_TO_EXCEL_DASHBOARDS,
    ]
)


SECTION_C = QuickStartSection(
    title=ugettext_lazy("Optimize field worker performance"),
    cards=[
        cards.CUSTOMIZE_ACCESS,
        cards.MONITOR_YOUR_WORKFORCE,
        cards.TRIGGER_SMS_REMINDERS,
        cards.GUIDE_FIELD_WORKERS,
    ]
)


SECTION_D = QuickStartSection(
    title=ugettext_lazy("Enable complex data collection"),
    cards=[
        cards.BUILD_DYNAMIC_FORMS,
        cards.AUTOMATE_DATA_COLLECTION,
        cards.PRIORITIZE_TASKS,
        cards.ELIMINATE_DUPLICATE_DATA,
    ]
)


AREA = QuickStartArea(
    title=ugettext_lazy("Monitor and Evaluate Your Program"),
    slug='monitoring-evaluation',
    sections=[
        SECTION_A,
        SECTION_B,
        SECTION_C,
        SECTION_D,
    ]
)
