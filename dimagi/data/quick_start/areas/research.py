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
    title=ugettext_lazy("Collect and analyze clean data"),
    cards=[
        cards.INSPECT_YOUR_DATA,
        cards.CORRECT_DATA_ERRORS,
        cards.EXPORT_DATA_FOR_ANALYSIS,
        cards.MONITOR_CHANGES_OVER_TIME,
        cards.ELIMINATE_DUPLICATE_DATA,
    ]
)


SECTION_C = QuickStartSection(
    title=ugettext_lazy(
        "Ensure field workers follow data collection guidelines"
    ),
    cards=[
        cards.CUSTOMIZE_ACCESS,
        cards.MONITOR_YOUR_WORKFORCE,
        cards.GUIDE_FIELD_WORKERS,
        cards.TRIGGER_SMS_REMINDERS,
    ]
)


SECTION_D = QuickStartSection(
    title=ugettext_lazy("Build research protocols into your app"),
    cards=[
        cards.BUILD_DYNAMIC_FORMS,
        cards.AUTOMATE_DATA_COLLECTION,
        cards.PRIORITIZE_TASKS,
        cards.PERFORM_BACKGROUND_CALCULATIONS,
    ]
)


AREA = QuickStartArea(
    title=ugettext_lazy("Collect Research Data"),
    slug='research',
    description=ugettext_lazy(
        "Learn how to use CommCare to collect data for your research project."
    ),
    sections=[
        SECTION_A,
        SECTION_B,
        SECTION_C,
        SECTION_D,
    ]
)
