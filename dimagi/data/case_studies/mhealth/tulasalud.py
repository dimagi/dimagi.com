from __future__ import absolute_import
from django.utils.translation import ugettext_lazy
from dimagi.pages.models.case_studies import CaseStudy


STUDY = CaseStudy(
    title=ugettext_lazy(
        "TulaSalud: CommCare for Improving and Monitoring Community Health"
    ),
    summary=ugettext_lazy(
        "Guatemala’s northern highlands has one of the highest burdens of "
        "maternal mortality in the world due to a substantial majority of "
        "their population living below the poverty line and a severe lack "
        "of formal health services. To improve maternal care and reproductive "
        "health in Guatemala, TulaSalud introduced a digital health program "
        "for frontline health workers supported by CommCare. In collaboration "
        "with the Guatemalan Ministry of Health, the organization has "
        "enhanced its community-based digital health program by expanding "
        "its network of care beyond Alta Verapaz to three additional priority "
        "regions (Huehuetenango, Quiché, and Sololà) and increasing "
        "accountability at all levels."
    ),
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
    download_url="https://www.dropbox.com/s/gehewi5z55xkaw3/mhealth-guatemala-childhealth.pdf?dl=1",
    hubspot_form="6735a7d4-2701-4b7f-9bf7-46183a8bba53",
)
