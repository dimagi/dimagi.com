from __future__ import absolute_import
from django.utils.translation import ugettext_lazy
from dimagi.pages.models.case_studies import CaseStudy


STUDY = CaseStudy(
    title=ugettext_lazy(
        "Focus Region Health Project: Reducing Stock Outs for Reproductive "
        "Health Products"
    ),
    summary=[
        ugettext_lazy(
            "The Focus Region Health Project’s Early Warning System was designed "
            "to provide real-time stock status information on reproductive health "
            "commodities to provide early warning of a dip in supplies. Its "
            "automated, data-focused approach fosters effective supervision of "
            "ordering and delivery to ensure that essential health commodities are "
            "always available by facilitating consistent, planned orders and "
            "avoiding widespread emergency orders."
        ),
    ],
    partners=[
        "JSI Research & Training Institute, Inc.",
        "Ghana Health Services",
        "USAID Deliver Project",
    ],
    countries=[
        ugettext_lazy("Ghana"),
    ],
    sectors=[
        ugettext_lazy("Maternal & Child Health"),
        ugettext_lazy("Infectious Disease"),
    ],
    features=[
        ugettext_lazy("Custom Reports"),
        ugettext_lazy("SMS Notifications"),
        ugettext_lazy("Location-based Messaging and Report Access"),
        ugettext_lazy("Web and SMS-based Form Input"),
    ],
    slug="mhealth-supply-chain-ghana",
    primary_cta="c87364f1-18d5-4355-ba2d-a6e1bcdee20c",
    subnav_cta="3bbb492a-116d-4cfe-b002-66ce653cb738",
    event_tracking_title="Focus Region Health Project",
)
