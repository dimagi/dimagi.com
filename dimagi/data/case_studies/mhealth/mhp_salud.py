from __future__ import absolute_import
from django.utils.translation import ugettext_lazy
from dimagi.pages.models.case_studies import CaseStudy


STUDY = CaseStudy(
    title=ugettext_lazy(
        "MHP Salud: CommCare for an Integrated Approach to Improving "
        "Community Health"
    ),
    summary=[
        ugettext_lazy(
            "For the last 35 years, nonprofit organization MHP Salud has "
            "implemented Community Health Worker (CHW) programs to support "
            "underserved Latino communities across the United States. From case "
            "management for older adults to assistance navigating the Health "
            "Insurance Marketplace, MHP Salud’s CommCare application keeps track "
            "of participants across various community-based health initiatives, "
            "including referrals to external organizations."
        ),
        ugettext_lazy(
            "MHP Salud has increased enrollment in public assistance and health "
            "insurance programs and continues to offer support to over 5,000 "
            "Latino Americans annually struggling with mental health issues, chronic "
            "disease, and other health challenges."
        ),
    ],
    partners=[
        "MHP Salud",
    ],
    countries=[
        ugettext_lazy("United States"),
    ],
    sectors=[
        ugettext_lazy("Maternal & Child Health"),
        ugettext_lazy("Nutrition"),
        ugettext_lazy("Gender-Based Violence"),
    ],
    features=[
        ugettext_lazy("Case Management"),
        ugettext_lazy("Referrals"),
        ugettext_lazy("Data Collection"),
        ugettext_lazy("Conditional Alerts"),
    ],
    slug="mhp-salud",
    primary_cta="cc32b07a-4bdd-46f7-8a0e-934a7312af03",
    subnav_cta="37eea299-19a1-4d98-8484-41ebd52114a9",
    event_tracking_title="MHP Salud",
)
