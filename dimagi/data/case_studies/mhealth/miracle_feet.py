from __future__ import absolute_import
from django.utils.translation import ugettext_lazy
from dimagi.pages.models.case_studies import CaseStudy


STUDY = CaseStudy(
    title=ugettext_lazy(
        "MiracleFeet: CommCare for Treating Congenital Defects"
    ),
    summary=[
        ugettext_lazy(
            "With funding from a $1M grant from Google.org, MiracleFeet commissioned "
            "Dimagi to create a universal tool to track treatment and program data "
            "for clubfoot, a common and treatable birth defect historically overlooked "
            "in many low- and middle-income countries (LMICs). Currently, only one in "
            "five children globally has access to care—making it a leading cause of "
            "physical disability worldwide. In ten years, MiracleFeet has developed "
            "systems and partnerships to treat clubfoot in 29 countries, where over "
            "75,000 new cases occur each year. "
        ),
        ugettext_lazy(
            "MiracleFeet selected CommCare to create a streamlined data collection "
            "tool, the Clubfoot Administration System (CAST), in support of its growing "
            "global network of clinics and providers who are increasing access to this "
            "critical treatment. Ninety-five percent of MiracleFeet-supported clinics "
            "have adopted the application, with CAST now in use in 371 clinics across "
            "29 countries, storing nearly 41,000 patient records that document full "
            "treatment progress and outcomes."
        ),
    ],
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
    primary_cta="d6678fcd-19ba-4953-9104-ad4ce6eb8b46",
    subnav_cta="09ce8a2d-067a-457d-891d-e2ee6938d3ce",
    event_tracking_title="MiracleFeet",
)
