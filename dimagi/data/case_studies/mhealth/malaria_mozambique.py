from __future__ import absolute_import
from django.utils.translation import ugettext_lazy
from dimagi.pages.models.case_studies import CaseStudy


STUDY = CaseStudy(
    title=ugettext_lazy(
        "Malaria Consortium upSCALE: iCCM for Improving Child Health "
    ),
    summary=[
        ugettext_lazy(
            "upSCALE supports community health workers (CHWs) in Mozambique to "
            "deliver integrated community case management (iCCM) in the remote "
            "communities that they serve. The CHWs use a smartphone-based "
            "application, built on the CommCare platform, to guide them through "
            "the patient consultation. The program adopted CommCare to strengthen "
            "communication between CHWs and health facility supervisors. "
        ),
        ugettext_lazy(
            "With the Ministry of Health staff now taking on responsibility for "
            "content design, training, rollout, and platform hosting, upSCALE "
            "has the potential to expand into other areas of the health system, "
            "with the goal of improved diagnosis, treatment, and monitoring of "
            "disease throughout Mozambique."
        ),
    ],
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
        ugettext_lazy("Infectious Disease"),
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
    primary_cta="da75e85e-fa80-4176-9202-a5818292f699",
    subnav_cta="fd837f8b-ab6e-4f50-a205-9d26d1512c97",
    event_tracking_title="Malaria Consortium upSCALE",
    download_url_language="https://cdn2.hubspot.net/hubfs/503070/Case%20Studies/CommCare%20-%20Malaria%20Consortium%20Case%20Study_French.pdf",
    hubspot_form_language="8281faf9-4e54-49a9-9090-fe2fa57cf4a8",
    theme = "orange-theme",
)
