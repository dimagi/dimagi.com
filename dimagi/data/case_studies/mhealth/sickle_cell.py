from __future__ import absolute_import
from django.utils.translation import ugettext_lazy
from dimagi.pages.models.case_studies import CaseStudy


STUDY = CaseStudy(
    title=ugettext_lazy(
        "Sickle Cell Foundation: CommCare for Mitigating "
        "Child Deaths from Hereditary Disease"
    ),
    summary=[
        ugettext_lazy(
            "Every year, upwards of 400,000 children are born with Sickle Cell "
            "Disease (SCD), a genetic disease that stiffens red blood cells and "
            "distorts their normal round shape, causing many complications including, "
            "frequent episodes of pain, acute lung injury, stroke, overwhelming "
            "infection, and chronic organ damage. Three-quarters of these children live "
            "in sub-Saharan Africa. Further, the World Health Organization (WHO) estimates "
            "that 70% of deaths associated with SCD are preventable with simple, "
            "cost-effective interventions, such as early detection through newborn screening "
            "and the subsequent provision of comprehensive care." 
        ),
        ugettext_lazy(
            "Since 2017, Dimagi has partnered with the Sickle Cell Foundation of "
            "Ghana (SCFG) to support the National Newborn Screening Program (NNSP) "
            "by digitizing its paper forms and serving as a job aid to its users. To "
            "date, more than 12,500 newborns have been registered through the mobile "
            "application at six sites across two districts in Ghana."
        ),
    ],
    partners=[
        "Sickle Cell Foundation of Ghana",
        "Novartis, Ministry of Health (Ghana)",
        "Ghana Health Service",
    ],
    countries=[
        ugettext_lazy("Ghana"),
    ],
    sectors=[
        ugettext_lazy("Disease Treatment"),
        ugettext_lazy("Maternal & Child Health"),
    ],
    features=[
        ugettext_lazy("Offline Case Management"),
        ugettext_lazy("Multimedia"),
        ugettext_lazy("Validation Conditions"),
        ugettext_lazy("Custom User Properties"),
        ugettext_lazy("Case Sharing"),
        ugettext_lazy("Case List Filters"),
        ugettext_lazy("Automatic Case Closure"),
    ],
    slug="sickle-cell",
    primary_cta="57e73298-f60f-4139-9198-a62e799fa0a3",
    subnav_cta="9acba66c-efef-40d2-a06f-defb2b4fedbf",
    event_tracking_title="Sickle Cell Foundation",
)
