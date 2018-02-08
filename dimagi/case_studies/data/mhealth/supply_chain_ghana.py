from __future__ import absolute_import
from django.utils.translation import ugettext_lazy
from dimagi.case_studies.models import CaseStudy


STUDY = CaseStudy(
    title=ugettext_lazy(
        "Improving Reproductive Health Commodities Stock Tracking in Ghana"
    ),
    summary=ugettext_lazy(
        "In 2009, the Focus Region Health Project (FRHP), implemented by "
        "JSI Research & Training Institute Inc., in collaboration with "
        "Ghana Health Services (GHS) and the USAID | DELIVER PROJECT, "
        "engaged with Dimagi to design and implement the Early Warning "
        "System. This system was designed to provide real-time stock "
        "status information on reproductive health commodities to decision-"
        "makers at all levels and to provide early warning of a dip in "
        "supplies. Its goal was also to foster effective supervision of "
        "ordering and delivery, reinforce the availability of all essential "
        "health commodities by improving the timeliness and accuracy of "
        "paper-based ordering and reporting from the SDPs, prevent widespread "
        "emergency ordering by aiding districts and facilities in planned "
        "ordering through effective, automated data analysis tools."
    ),
    partners=[
        "JSI Research & Training Institute",
        "Ghana Health Services",
        "USAID",
        "Dimagi",
    ],
    countries=[
        ugettext_lazy("Ghana"),
    ],
    sectors=[
        ugettext_lazy("Supply Chain Management"),
    ],
    features=[],
    slug="mhealth-supply-chain-ghana",
    download_url="https://www.dropbox.com/s/5zvsxd2jb38p3t4/mhealth-supply-chain-ghana.pdf?dl=1",
)
