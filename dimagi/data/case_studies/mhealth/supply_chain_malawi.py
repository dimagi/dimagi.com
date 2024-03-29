from __future__ import absolute_import
from django.utils.translation import ugettext_lazy
from dimagi.pages.models.case_studies import CaseStudy


STUDY = CaseStudy(
    title=ugettext_lazy(
        "cStock: Supply Chains for Community Case Management"
    ),
    summary=[
        ugettext_lazy(
            "In Malawi, the Ministry of Health and Population (MoHP) is "
            "championing the strengthening of community health systems. As part "
            "of this effort, the MoHP enlists the support of Health Surveillance "
            "Assistants (HSAs), who assess and treat minor conditions for "
            "children under five, which requires them to be well stocked on "
            "essential, life-saving medicines. To help them with this, the MoHP "
            "introduced the “cStock” tool that allowed greater visibility into "
            "community level data continues to be implemented under the Ministry "
            "of Health and Population leadership todate, with funding from Global "
            "Fund that is being managed by the World Vision Malawi."
        ),
    ],
    partners=[
        "JSI Research & Training Institute, Inc.,",
        "Bill & Melinda Gates Foundation",
        "Malawi Ministry of Health",
        "Global Fund",
        "World Vision International (Malawi)",
    ],
    countries=[
        ugettext_lazy("Malawi"),
    ],
    sectors=[
        ugettext_lazy("Disease Treatment and Prevention"),
        ugettext_lazy("Maternal & Child Health"),
    ],
    features=[
        ugettext_lazy("SMS-based Form Input"),
    ],
    slug="mhealth-supply-chain-malawi",
    primary_cta="8ec3dce3-f4f3-4105-87c5-1ba29d86457f",
    subnav_cta="75b947cf-de55-43c7-b46d-ae42f49a6c7f",
    event_tracking_title="cStock",
    theme = "orange-theme",
)
