from __future__ import absolute_import
from django.utils.translation import ugettext_lazy
from dimagi.pages.models.case_studies import CaseStudy


STUDY = CaseStudy(
    title=ugettext_lazy(
        "Focus Region Health Project: Reducing Stock Outs for Reproductive "
        "Health Products"
    ),
    summary=ugettext_lazy(
        "The Focus Region Health Project’s Early Warning System was designed "
        "to provide real-time stock status information on reproductive health "
        "commodities to provide early warning of a dip in supplies. Its "
        "automated, data-focused approach fosters effective supervision of "
        "ordering and delivery to ensure that essential health commodities is "
        "always be available by facilitating consistent, planned ordering and "
        "avoiding widespread emergency orders."
    ),
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
        ugettext_lazy("Disease Treatment"),
    ],
    features=[
        ugettext_lazy("Custom Reports"),
        ugettext_lazy("SMS Notifications"),
        ugettext_lazy("Location-based Messaging and Report Access"),
        ugettext_lazy("Web and SMS-based Form Input"),
    ],
    slug="mhealth-supply-chain-ghana",
    download_url="https://www.dropbox.com/s/5zvsxd2jb38p3t4/mhealth-supply-chain-ghana.pdf?dl=1",
    hubspot_form="9b30bfc9-2b46-414b-b551-8a25038a1073",
)
