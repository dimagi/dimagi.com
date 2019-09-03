from __future__ import absolute_import
from django.utils.translation import ugettext_lazy
from dimagi.pages.models.case_studies import CaseStudy


STUDY = CaseStudy(
    title=ugettext_lazy(
        "Naatal Mbay: CommCare for Agricultural Support"
    ),
    summary=ugettext_lazy(
        "Naatal Mbay, which means “making agriculture prosperous,” is a Feed "
        "the Future project that uses digital tools to empower farmer-serving "
        "organizations active in the rice, maize, and millet value chains in "
        "Senegal. The program uses CommCare to support locally-owned and "
        "sustainable data collection by tracking inputs and productivity, "
        "managing loans, and collecting rainfall data monitoring – while "
        "increasing transparency along the chain and attracting investment. "
        "CommAgri, Naatal Mbay’s digital tool, is used by 55 cooperatives and "
        "500 extension agents, who have registered 68,000 farmers."
    ),
    partners=[
        "RTI",
        "Feed the Future",
        "USAID",
    ],
    countries=[
        ugettext_lazy("Senegal"),
    ],
    sectors=[
        ugettext_lazy("Agricultural Cooperatives"),
        ugettext_lazy("Agricultural Logistics"),
    ],
    features=[
        ugettext_lazy("Case Management"),
        ugettext_lazy("CommCare Supply"),
        ugettext_lazy("Area Mapper"),
    ],
    slug="naatal-mbay",
    download_url="https://www.dropbox.com/s/oakh337uexf4zgj/mhealth-tdh-burkinafaso.pdf?dl=1",
    hubspot_form="2f9b7c9b-1723-4273-87ff-487d6b5d0564",
)
