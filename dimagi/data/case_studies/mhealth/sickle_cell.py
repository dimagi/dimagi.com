from __future__ import absolute_import
from django.utils.translation import ugettext_lazy
from dimagi.pages.models.case_studies import CaseStudy


STUDY = CaseStudy(
    title=ugettext_lazy(
        "Sickle Cell Foundation: CommCare for Mitigating "
        "Child Deaths from Hereditary Disease"
    ),
    summary=ugettext_lazy(
        "Every year, upwards of 400,000 children are born with Sickle Cell "
        "Disease (SCD), a genetic disease that stiffens red blood cells and "
        "distorts their normal round shape, causing many complications including, "
        "frequent episodes of pain, acute lung injury, stroke, overwhelming "
        "infection, and chronic organ damage. Three-quarters of these children live "
        "in sub-Saharan Africa. Further, the World Health Organization (WHO) estimates "
        "that 70% of deaths associated with SCD are preventable with simple, "
        "cost-effective interventions, such as early detection through newborn screening "
        "and the subsequent provision of comprehensive care." 
        "Since 2017, Dimagi has partnered with the Sickle Cell Foundation of "
        "Ghana (SCFG) to support the National Newborn Screening Program (NNSP) "
        "by digitizing its paper forms and serving as a job aid to its users. To "
        "date, more than 12,500 newborns have been registered through the mobile "
        "application at six sites across two districts in Ghana."
    ),
    partners=[
        "Novartis, Ministry of Health (Ghana)",
        "Ghana Health Service",
        "Sickle Cell Foundation of Ghana",
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
    download_url="https://f.hubspotusercontent20.net/hubfs/503070/Case%20Studies/CommCare%20-%20Sickle%20Cell%20Foundation%20Case%20Study.pdf",
    hubspot_form="1c787f58-b720-4dd7-af0f-4f6b8d63093c",
)
