from __future__ import absolute_import
from django.utils.translation import ugettext_lazy
from dimagi.case_studies.models import CaseStudy


STUDY = CaseStudy(
    title=ugettext_lazy(
        "Using Mobile Rapid Diagnostic Tests for HIV and Malaria in Zimbabwe"
    ),
    summary=ugettext_lazy(
        "With support from Econet Wireless and the Zimbabwean Ministry "
        "of Health, Global Solutions for Infectious Diseases (GSID) "
        "created a mobile system with Dimagi and ODK Diagnostics to "
        "better process rapid diagnostic tests for HIV and malaria. "
        "The system utilizes CommCare’s case management and reporting "
        "features to digitize health workers’ workloads, and ODK-Dx’s "
        "ability to process, analyze, and return RDT results with computer "
        "vision algorithms."
    ),
    partners=[
        "Zimbabwe Global Solutions for Infectious Diseases",
    ],
    countries=[
        ugettext_lazy("Zimbabwe"),
    ],
    sectors=[
        ugettext_lazy("Malaria & HIV/AIDS"),
    ],
    features=[
        ugettext_lazy("Data collection"),
        ugettext_lazy("automatic reporting"),
        ugettext_lazy("RDT capturing & analysis"),
        ugettext_lazy("health worker supervision"),
        ugettext_lazy("process adherence"),
    ],
    slug="mhealth-hiv-zimbabwe",
)
