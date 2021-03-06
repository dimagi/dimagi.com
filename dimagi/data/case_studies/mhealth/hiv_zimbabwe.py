from __future__ import absolute_import
from django.utils.translation import ugettext_lazy
from dimagi.pages.models.case_studies import CaseStudy


STUDY = CaseStudy(
    title=ugettext_lazy(
        "Global Solutions for Infectious Diseases: Reporting Rapid "
        "Diagnostic Test Results"
    ),
    summary=[
        ugettext_lazy(
            "With support from Econet Wireless and the Zimbabwean Ministry of "
            "Health, Global Solutions for Infectious Diseases (GSID) created a "
            "mobile system with Dimagi and ODK Diagnostics to better process "
            "rapid diagnostic tests for HIV and malaria. "
        ),
        ugettext_lazy(
            "The system utilizes CommCare’s case management and reporting features "
            "to digitize health workers’ workloads, and ODK-Dx’s ability to "
            "process, analyze, and return RDT results with computer vision algorithms."
        ),
    ],
    partners=[
        "Global Solutions for Infectious Diseases (GSID)",
        "Zimbabwe Ministry of Health",
        "Econet Wireless",
    ],
    countries=[
        ugettext_lazy("Zimbabwe"),
    ],
    sectors=[
        ugettext_lazy("Infectious Disease"),
    ],
    features=[
        ugettext_lazy("Data Collection"),
        ugettext_lazy("Automatic Reporting"),
        ugettext_lazy("RDT Capturing & Analysis"),
        ugettext_lazy("Health Worker Supervision"),
        ugettext_lazy("Process Adherence"),
    ],
    slug="mhealth-hiv-zimbabwe",
    primary_cta="6c6b7a29-63c4-4c99-996a-4675929d5a95",
    subnav_cta="d1f6cde7-968e-41e7-8a57-f7fa5273c5a7",
    event_tracking_title="Global Solutions for Infectious Disease",
)
