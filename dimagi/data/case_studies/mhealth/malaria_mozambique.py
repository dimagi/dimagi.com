from __future__ import absolute_import
from django.utils.translation import ugettext_lazy
from dimagi.pages.models.case_studies import CaseStudy


STUDY = CaseStudy(
    title=ugettext_lazy(
        "Malaria Consortium upSCALE: iCCM for Improving Child Health "
    ),
    summary=ugettext_lazy(
        "upSCALE supports community health workers (CHWs) in Mozambique to "
        "deliver integrated community case management (iCCM) in the remote "
        "communities that they serve. The CHWs use a smartphone-based "
        "application, built on the CommCare platform, to guide them through "
        "the patient consultation. The program adopted CommCare to strengthen "
        "communication between CHWs and health facility supervisors. With "
        "the Ministry of Health staff now taking on responsibility for "
        "content design, training, rollout, and platform hosting, upSCALE "
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
