from __future__ import absolute_import
from django.utils.translation import ugettext_lazy
from dimagi.pages.models.case_studies import CaseStudy


STUDY = CaseStudy(
    title=ugettext_lazy(
        "Terre des hommes: The Integrated eDiagnostic Approach for Child Health"
    ),
    summary=[
        ugettext_lazy(
            "As part of their Integrated eDiagnostic Approach, Terre des hommes "
            "partnered with Dimagi to create a tablet-based application known as "
            "the Electronic Register of Consultations (REC). Built on Dimagi’s "
            "CommCare platform, the REC aims to increase nurses’ adherence to "
            "IMCI protocols and improve their quality of care by providing "
            "enhanced decision support and case management capacity. "
        ),
        ugettext_lazy(
            "More than 4,000 community health workers use the REC to treat around 200,000 "
            "children every month in 729 clinics across the country. The program "
            "has been so successful that it is being transitioned to "
            "Ministry of Health ownership."
        ),
    ],
    partners=[
        "Terre des Hommes",
        "Burkina Faso Ministry of Health",
        "London School of Hygiene and Tropical Medicine (LSHTM)",
        "the University -Research Company (URC)",
    ],
    countries=[
        ugettext_lazy("Burkina Faso"),
    ],
    sectors=[
        ugettext_lazy("Maternal & Child Health"),
    ],
    features=[
        ugettext_lazy("Data Collection"),
        ugettext_lazy("Case Management"),
        ugettext_lazy("Decision & Diagnostic Support"),
        ugettext_lazy("HIPAA Compliance"),
        ugettext_lazy("Custom Reports"),
        ugettext_lazy("clinical workflows"),
        ugettext_lazy("Multimedia"),
        ugettext_lazy("Data Validation"),
    ],
    slug="mhealth-tdh-burkinafaso",
    primary_cta="74b536b6-b601-476a-9bd2-08fc326ab597",
    subnav_cta="37f12183-8eef-48b9-b933-a9796aab8bbf",
    event_tracking_title="Terre des hommes",
    theme = "orange-theme",
)
