from __future__ import absolute_import
from django.utils.translation import ugettext_lazy
from dimagi.case_studies.models import CaseStudy


STUDY = CaseStudy(
    title=ugettext_lazy(
        "Leveraging SMS to Inform Supply Chain in Tanzania"
    ),
    summary=ugettext_lazy(
        "As part of a larger effort to integrate and streamline "
        "logistics management in Tanzania, the USAID | DELIVER PROJECT "
        "and the Ministry of Health and Social Welfare (MOHSW) established "
        "the ILSGateway in 2008 in order to expand accessibility and "
        "visibility of logistics data to inform supply chain decision "
        "making through mobile technology."
    ),
    partners=[
        "Tanzania Ministry of Health",
        "USAID | DELIVER Project",
        "Dimagi",
    ],
    countries=[
        ugettext_lazy("Tanzania"),
    ],
    sectors=[
        ugettext_lazy("Supply Chain Management"),
    ],
    features=[],
    slug="mhealth-supply-chain-tanzania",
)
