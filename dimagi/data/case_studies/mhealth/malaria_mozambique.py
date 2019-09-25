from __future__ import absolute_import
from django.utils.translation import ugettext_lazy
from dimagi.pages.models.case_studies import CaseStudy


STUDY = CaseStudy(
    title=ugettext_lazy(
        "Malaria Consortium upSCALE: iCCM for Improving Child Health "
    ),
    summary=ugettext_lazy(
        "The upSCALE project uses Integrated Community Case Management "
        "(iCCM) to improve healthcare services and expand coverage in "
        "Mozambique, a country where only 52% of the population has "
        "healthcare coverage. The project adopted CommCare to strengthen "
        "communication between community health workers (CHWs) and health "
        "facility supervisors. With Ministry of Health staff now responsible "
        "for content design, training, rollout, and platform hosting, upSCALE "
        "has the potential to expand into other areas of the health system, "
        "with the goal of improved diagnosis, treatment, and monitoring of "
        "disease throughout Mozambique."
    ),
    partners=[
        "Mozambique Ministry of Health",
        "Malaria Consortium",
        "UNICEF",
    ],
    countries=[
        ugettext_lazy("Mozambique"),
    ],
    sectors=[
        ugettext_lazy("Maternal & Child Health"),
        ugettext_lazy("Disease Treatment"),
    ],
    features=[
        ugettext_lazy("Case Management"),
        ugettext_lazy("Decision & Diagnostic Support"),
        ugettext_lazy("Respiratory Rate Counter"),
        ugettext_lazy("SMS Notifications"),
        ugettext_lazy("Multimedia"),
        ugettext_lazy("Custom Reporting"),
    ],
    slug="mhealth-malaria-mozambique",
    download_url="https://cdn2.hubspot.net/hubfs/503070/Case%20Studies/CommCare%20-%20Malaria%20Consortium%20Case%20Study.pdf",
    hubspot_form="e39f88d8-e985-44bd-92ff-48a382bed12b",
)
