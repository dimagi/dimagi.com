from __future__ import absolute_import
from django.utils.translation import ugettext_lazy
from dimagi.pages.models.case_studies import CaseStudy


STUDY = CaseStudy(
    title=ugettext_lazy(
        "MiracleFeet: CommCare for Treating Congenital Defects"
    ),
    summary=ugettext_lazy(
        "With funding from a $1M grant from Google.org, MiracleFeet commissioned "
        "Dimagi to create a universal tool to track treatment and program data for "
        "clubfoot, a common birth defect routinely treated in wealthy countries but "
        "historically overlooked in many low- and middle-income countries (LMICs). The "
        "condition is fully treatable, but currently only one in five children globally "
        "has access to care—making it a leading cause of physical disability worldwide. "
        "In ten years, MiracleFeet has developed systems and partnerships to treat clubfoot "
        "in 27 countries, where over 70,000 new cases occur each year. MiracleFeet needed a "
        "streamlined data collection tool to support and monitor its growing global network "
        "of clinics and providers who are increasing access to this critical treatment."
        "In late 2019, MiracleFeet completed the global rollout of the Clubfoot "
        "Administration System (CAST). The mobile app is transforming MiracleFeet’s "
        "ability to monitor treatment quality and to strategically plan and scale programs "
        "to reach populations that lack access to the proven, low-cost method of care. The "
        "tool syncs with Salesforce to render user-friendly dashboards with sophisticated "
        "analytics and reporting capabilities. This system amplifies and enhances all "
        "stakeholders’ focus on treatment precision and quality, from program managers "
        "to country partners and clinicians. Nintey-five percent of MiracleFeet-supported "
        "clinics have adopted the application, with CAST now in use in 371 clinics across "
        "29 countries, storing nearly 41,000 patient records that document full treatment "
        "progress and outcomes."
    ),
    partners=[
        "MiracleFeet",
        "Google.org"
    ],
    countries=[
        ugettext_lazy("29 countries across Africa, Asia, and Latin America"),
    ],
    sectors=[
        ugettext_lazy("Child Health"),
    ],
    features=[
        ugettext_lazy("Offline Case Management"),
        ugettext_lazy("Multimedia"),
        ugettext_lazy("Validation Conditions"),
        ugettext_lazy("Case List Filters"),
    ],
    slug="miracle-feet",
    download_url="https://f.hubspotusercontent20.net/hubfs/503070/Case%20Studies/CommCare%20-%20MiracleFeet%20Case%20Study.pdf",
    hubspot_form="d886f97e-d29e-4ed1-a20c-70bddabc2ea7",
)
