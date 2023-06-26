from __future__ import absolute_import
from django.utils.translation import ugettext_lazy
from dimagi.pages.models.case_studies import CaseStudy


STUDY = CaseStudy(
    title=ugettext_lazy(
        "TulaSalud: CommCare for Improving and Monitoring Community Health"
    ),
    summary=[
        ugettext_lazy(
            "Guatemala’s northern highlands has one of the highest burdens of "
            "maternal mortality in the world due to a substantial majority of "
            "their population living below the poverty line and a severe lack "
            "of formal health services. To improve maternal care and reproductive "
            "health in Guatemala, TulaSalud introduced a digital health program "
            "for frontline health workers supported by CommCare."
        ),
        ugettext_lazy(
            "In collaboration with the Guatemalan Ministry of Health, the organization has "
            "enhanced its community-based digital health program by expanding "
            "its network of care beyond Alta Verapaz to three additional priority "
            "regions (Huehuetenango, Quiché, and Sololà) and increasing "
            "accountability at all levels."
        ),
    ],
    partners=[
        "TulaSalud",
        "Tula Foundation",
        "Guatemalan Ministry of Health",
        "Government of Canada (via Global Affairs Canada)",
    ],
    countries=[
        ugettext_lazy("Guatemala"),
    ],
    sectors=[
        ugettext_lazy("Maternal, Newborn & Child Health (MNCH)"),
        ugettext_lazy("Sexual and Reproductive Health and Rights (SRHR)"),
    ],
    features=[
        ugettext_lazy("Case Management"),
        ugettext_lazy("Decision & Diagnostic Support"),
        ugettext_lazy("WHO Z-scores"),
        ugettext_lazy("Clinical Workflow"),
        ugettext_lazy("Custom Reports"),
        ugettext_lazy("Transportation Coordination"),
        ugettext_lazy("Referral Follow-up"),
    ],
    slug="tulasalud-mnch",
    primary_cta="4ecfc35a-3cc9-4e43-8223-25a017002a17",
    subnav_cta="a6c3588a-d194-433d-9778-9cd84d1866e9",
    event_tracking_title="TulaSalud",
    theme = "orange-theme",
)
